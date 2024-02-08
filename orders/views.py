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
# code 
from utils.generate_code import generate_code


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
    total = round(sub_total + delivery_fee,2)
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
                html = render_to_string('includes/coupon-check.html',{
                    'cart':cart ,
                    'cart_detail':cart_detail,
                    'delivery_fee' : delivery_fee,
                    'sub_total' : round(sub_total,2),
                    'total' : total,
                    'discount': round(coupon_value,2),
                    'pub_key':pub_key,
                })
                return JsonResponse({'result':html})                
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
    cart = Cart.objects.get(user=request.user,status='inprogress')
    cart_detail = CartDetail.objects.filter(cart=cart)
    delivery_fee= DeliveryFee.objects.last().fee

    if cart.order_total_discount:
        total = cart.order_total_discount() + delivery_fee
    else:
        total = cart.cart_total() + delivery_fee
    
    code = generate_code()
    # store code in session
    request.session['order_code'] = code
    request.session.save()

    stripe.api_key = env('STRIP_API_KEY_SECRET')


    checkout_session = stripe.checkout.Session.create(
        line_items=[
            {
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': code
                    },
                    'unit_amount': int(total*100)
                },
                'quantity': 1
            },
        ],
        mode='payment',
        success_url= 'http://127.0.0.1:8000/orders/checkout/payment/success',
        cancel_url= 'http://127.0.0.1:8000/orders/checkout/payment/failed'
    )

    return JsonResponse({'session':checkout_session})



@login_required
def payment_success(request):
    cart = Cart.objects.get(user=request.user,status='inprogress')
    cart_detail = CartDetail.objects.filter(cart=cart)

    # get code from the session
    order_code = request.session.get('order_code')

    # cart-------------> order
    new_order = Order.objects.create(
        user = request.user ,
        coupon = cart.coupon,
        order_total_discount = cart.order_total_discount,
        code = order_code     
    )
    # cart_detail-------------> order_detail
    for object in cart_detail:
        OrderDetail.objects.create(
            order = new_order ,
            product = object.product ,
            quantity = object.quantity ,
            price = object.product.price ,
            total = object.total
        )
    cart.status= 'completed'
    cart.save()  

    return render(request, 'orders/success.html', {'code':order_code})

@login_required
def payment_failed(request):

    return render(request, 'orders/failed.html', {})

