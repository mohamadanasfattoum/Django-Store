import datetime
from django.shortcuts import render, redirect
from .models import Order, OrderDetail, Cart, CartDetail, Coupon
from settings.models import DeliveryFee
from django.shortcuts import get_object_or_404
from products.models import Product

def order_list(request):
    orders= Order.objects.all()
    return render(request,'orders/orders.html',{'orders':orders})


def checkout(request):
    cart = Cart.objects.get(user=request.user,status='inprogress')
    cart_detail= CartDetail.objects.filter(cart=cart)
    delivery_fee= DeliveryFee.objects.last().fee
    sub_total = cart.cart_total()
    total = sub_total + delivery_fee
    discount= 0


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

                })                



    return render(request,'orders/checkout.html',{
        'cart':cart ,
        'cart_detail':cart_detail,
        'delivery_fee' : delivery_fee,
        'sub_total' : sub_total,
        'total' : total,
        'discount': discount,

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
    cart_detail.total = round(quantity*product.price,2)
    cart_detail.save() 
    return redirect(f'/products/{product.slug}')