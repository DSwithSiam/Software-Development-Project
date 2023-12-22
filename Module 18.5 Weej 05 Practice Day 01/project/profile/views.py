from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib import messages
# Create your views here.

def user_register(request):
    if request.method =="POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def profile(request):
    if request.user.is_authenticated:
        # data = User.objects.get(username = request.user)
        data = request.user
        return render(request, 'profile.html', {'data': data})
    else:
        return redirect('user_login')
       

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_pass = form.cleaned_data['password']
            user = authenticate(username = user_name, password = user_pass)
            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in successful')
                return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form, 'type': "Login"})


def user_logout(request):
    logout(request)
    messages.success(request, 'Logged out Successful')
    return redirect('user_register')

def pass_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Change Your Password')
            update_session_auth_hash(request, form.user)
            return redirect('user_login')
        
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'login.html', {'form': form, 'type': "Change Password"})