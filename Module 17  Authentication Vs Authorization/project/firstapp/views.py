from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash


# Create your views here.
def signin(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                messages.success( request, 'Your account has been Created')
                form.save()
        else:
            form = RegisterForm()
        return render(request, 'signin.html', {"form": form})
    else:
        return redirect('profile')
        
        
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request = request, data = request.POST)
            if form.is_valid():
                name = form.cleaned_data['username']
                userpass = form.cleaned_data['password']
                user = authenticate(username = name, password = userpass) 
                if user is not None:
                    messages.success(request, 'Login successful')
                    login(request, user)
                    return redirect('profile')
        else:
            form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})
    else:
        return redirect('profile')
        
def profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = UserChangeData(request.POST, instance = request.user )
            if form.is_valid():
                form.save()
                messages.success(request, "Changes your Data")
                return redirect('profile')
        else:
            form = UserChangeData(instance = request.user )
        return render(request, 'profile.html', {'user': request.user, 'form': form})
    else:
        return redirect('login')
    
def user_logout(request):
    logout(request)
    return redirect('login')

def pass_change(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(user = request.user, data = request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect('profile')
        else:
            form = PasswordChangeForm(user = request.user)
        return render(request, 'pass_change.html', {'form': form})
    else:
        return redirect('login')
    
def pass_change2(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SetPasswordForm(user = request.user, data = request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect('profile')
        else:
            form = SetPasswordForm(user = request.user)
        return render(request, 'pass_change.html', {'form': form})
    else:
        return redirect('login')