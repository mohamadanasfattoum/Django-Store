import datetime
from django.shortcuts import render, redirect
from .models import Order, OrderDetail, Cart, CartDetail, Coupon
from settings.models import DeliveryFee
from django.shortcuts import get_object_or_404
from products.models import Product
import stripe
from django.conf import settings
from django.contrib.auth.decorators import login_required
# ajax
from django.http import JsonResponse
from django.template.loader import render_to_string
# env
from environ import Env
env = Env()
env.read_env()


@login_required
def order_list(request):
    orders= Order.objects.all()
    return render(request,'orders/orders.html',{'orders':orders})

@login_required
def checkout(request):
    cart = Cart.objects.get(user=request.user,status='inprogress')
    cart_detail= CartDetail.objects.filter(cart=cart)
    delivery_fee= DeliveryFee.objects.last().fee
    sub_total = cart.cart_total()
    total = sub_total + delivery_fee
    discount= 0
    pub_key = env('STRIP_API_KEY_PUBLISHABLE')


    if request.method == 'POST':
        code = request.POST['coupon_code'] # هيك بنادي عالكود من الصغحة
        #coupon = Coupon.objects.get(code=code)
        coupon = get_object_or_404(Coupon , code=code)    #لكي لايتوقف الموقع عند هدم تطابق الكود


        if coupon and coupon.quantity > 0 :  # للتأكد من الوقت 
            today_date = datetime.datetime.today().date()
            if today_date >= coupon.start_date and today_date <= coupon.end_date:
                coupon_value = sub_total / 100*coupon.discount
                sub_total = sub_total - coupon_value
                total = sub_total + delivery_fee

                cart.coupon = coupon
                cart.order_total_discount = sub_total # مجموع الخقم الرئيسي
                coupon.quantity -= 1
                cart.save()
                coupon.save()

                return render(request,'orders/checkout.html',{
                    'cart':cart ,
                    'cart_detail':cart_detail,
                    'delivery_fee' : delivery_fee,
                    'sub_total' : round(sub_total,2),
                    'total' : total,
                    'discount': round(coupon_value,2),
                    'pub_key':pub_key,

                })                



    return render(request,'orders/checkout.html',{
        'cart':cart ,
        'cart_detail':cart_detail,
        'delivery_fee' : delivery_fee,
        'sub_total' : sub_total,
        'total' : total,
        'discount': discount,
        'pub_key':pub_key,

    })


def add_to_cart(request):
    product = Product.objects.get(id=request.POST['product_id'])
    quantity = request.POST['quantity']

    cart = Cart.objects.get(user=request.user,status='inprogress')

    cart_detail , created = CartDetail.objects.get_or_create(cart=cart, product=product)

    # if not created:
    #     cart_detail.quantity = cart_detail.quantity + quantity

    cart_detail.price= product.price
    cart_detail.quantity = quantity
    cart_detail.total = round(int(quantity)*product.price,2)
    cart_detail.save() 

    cart = Cart.objects.get(user=request.user,status='inprogress')
    cart_detail = CartDetail.objects.filter(cart=cart)
    total = f'${cart.cart_total()}'
    cart_count = len(cart_detail)

    html = render_to_string('includes/cart_sidebar.html',{'cart_data':cart, 'cart_detail_data':cart_detail , request:request})
    return JsonResponse({'result':html, 'total':total, 'cart_count':cart_count})



def process_payment(request):
    checkout_session = stripe.checkout.Session.create(
        line_items=[
            {
                # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                'price': '{{PRICE_ID}}',
                'quantity': 1,
            },
        ],
        mode='payment',
        success_url=settings.DOMAIN + 'order/checkout/payment/success',
        cancel_url=settings.DOMAIN + 'order/checkout/payment/failed',
    )





@login_required
def payment_success(request):

    return render(request, 'orders/succes.html', {'code':'code'})

@login_required
def payment_failed(request):

    return render(request, 'orders/failed.html', {'code':'code'})

