from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import Login_form, Register_form
from django.contrib.auth.models import User
from .models import Custom_user


# Create your views here.


def login(request):
    form = Login_form(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            form.add_error('username', 'کاربری با این مشخصات یافت نشد')

    context = {

    }
    return render(request, 'login.html', context)


def register(request):
    form = Register_form(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        phone = form.cleaned_data.get('phone')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        User.objects.create(username=username, first_name=first_name, last_name=last_name, email=email,
                            password=password)
        user = User.objects.get(username=username)
        user.custom_user_set.create(phone=phone)
        return redirect('/login')

    context = {
        'form': form
    }
    return render(request, 'register.html', context)


def logout(request):
    logout(request)
    return redirect('/')
