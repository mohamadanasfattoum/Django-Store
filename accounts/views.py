from django.shortcuts import render, redirect
from .forms import SignupForm, ActivationForm
from django.contrib.auth.models import User
from .models import Profile
from django.core.mail import send_mail


def singup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        
        if form.is_valid():
            username= form.cleaned_data('username')
            email= form.cleaned_data('email')
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
    return render (request, 'registration/signup.html', {'form'=form})
    


def activate(request):
    pass
