from .models import Cart, CartDetail
# to show cart in all pages"
# and to add cart and return that one created it in all pages
# لأظهار واضافة واعادة اظهار الداتا المصافة في كل صفحة


def get_or_create_cart(request): # يا أما تجيب او تنشأ كارت
    if request.user.is_authenticated: # اذا المستخدم مسجل
        cart , created = Cart.objects.get_or_create(user=request.user,status='inprogress') # اذا الكارت موجودة اعرصها او غير موجودة انشاء كارت
        if not created:
            cart_detail = CartDetail.objects.filter(cart=cart)
            return {'cart_data':cart, 'cart_detail_data':cart_detail}
        return {'cart_data':cart}
    else:
        return {}