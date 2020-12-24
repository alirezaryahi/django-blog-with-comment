from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import Login_form, Register_form
from django.contrib.auth.models import User
from .models import Custom_user


# Create your views here.


def Login(request):
    if request.user.is_authenticated:
        return redirect('/')
    form = Login_form(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/allblog')
        else:
            form.add_error('username', 'کاربری با این مشخصات یافت نشد')

    context = {
        'form': form
    }
    return render(request, 'login.html', context)


def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    form = Register_form(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        phone = form.cleaned_data.get('phone')
        email = form.cleaned_data.get('email')
        User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email,
                                 password=password, is_superuser=True, is_active=True, is_staff=True)
        user = User.objects.get(username=username)
        Custom_user.objects.create(user_id=user.id, phone=phone)
        return redirect('/login')
        return redirect('/login')

    context = {
        'form': form
    }
    return render(request, 'register.html', context)


def Logout(request):
    logout(request)
    return redirect('/allblog')
