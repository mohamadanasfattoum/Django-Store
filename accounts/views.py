from django.shortcuts import render, redirect
from .forms import SignupForm, ActivationForm
from django.contrib.auth.models import User
from .models import Profile

from django.contrib.auth.decorators import login_required # لحتى مابدخل عالصفحة إلا المسجل دخول في الداشبورد

from django.core.mail import send_mail

from products.models import Product, Brand, Review
from orders.models import Order

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        
        if form.is_valid():
            username= form.cleaned_data['username']
            email= form.cleaned_data['email']

            user = form.save(commit=False)
            user.is_active = False



            form.save()
            # profile----> code
            profile = Profile.objects.get(user__username=username)
            send_mail(
                "Activate Your Account",
                f"Welcome {username} \nuse this code {profile.code} to activate your account",
                "samaanas30@gmail.com",
                [email],
                fail_silently=False,
            )
            return redirect(f'/accounts/{username}/activate')
    else:
        form = SignupForm()
    return render (request, 'registration/signup.html',  {'form':form})
    


def activate(request,username):
    profile = Profile.objects.get(user__username=username)
    if request.method == 'POST':
        form = ActivationForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            if code == profile.code:
                profile.code= ''

                user = User.objects.get(username=profile.user.username) # لتفعيل الحساب لما يتأكد من الكود ويساوي اكتف
                user.is_active = True
                user.save()
                profile.save()

                return redirect('/accounts/login')


    else:
        form = ActivationForm()
    return render (request, 'registration/activate.html', {'form':form})





@login_required # دللة تستخدم قبل دالة حتى تتفعل دالة الداش لازم يكون اليورس ريكوايرد
def dashboard(request):
    new_product = Product.objects.filter(flag ='New').count()
    feature_product = Product.objects.filter(flag ='Feature').count()
    sale_product = Product.objects.filter(flag ='Sale').count()

    user = User.objects.all().count
    order = Order.objects.all().count
    product = Product.objects.all().count
    brand = Brand.objects.all().count
    review = Review.objects.all().count


    return render(request,'accounts/dashboard.html', {
    'new_product':new_product ,
    'feature_product':feature_product,
    'sale_product':sale_product,
    
    'user':user,
    'order':order,
    'product':product,
    'brand':brand,
    'review':review,

    })