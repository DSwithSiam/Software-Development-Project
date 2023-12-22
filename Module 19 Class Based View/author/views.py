from typing import Any
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import *
from posts.models import Post
from django.contrib.auth.views import LoginView, LogoutView




def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account registration successful')
            return redirect('register')
    else:
        form = RegisterForm()
    return render(request, 'user_form.html', {'form': form, 'type': 'Register'})


# def user_login(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, request.POST)
#         if form.is_valid():
#             user_name = form.cleaned_data['username']
#             user_pass = form.cleaned_data['password']
#             user = authenticate(username = user_name, password = user_pass)
#             if user is not None:
#                 login(request, user)
#                 messages.success(request, 'Logged in successful')
#                 return redirect('profile')
#             else:
#                 messages.warning(request, 'Login information incorrect')
#                 return redirect('register')
#     else:
#         form = AuthenticationForm()
#     return render(request, 'user_form.html', {'form': form, 'type': 'Login'})

class userLoginView(LoginView):
    template_name = 'user_form.html'
   
    def get_success_url(self):
        return reverse_lazy('profile')
    
    def form_valid(self, form):
        messages.success(self.request, 'Login successful')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.success(self.request, 'Loggged in information incorrect')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context
        
        
        
# @login_required
# def user_logout(request):
#     if request.user.is_authenticated:
#         logout(request)
#     return redirect('login')


class UserLogoutView(LogoutView):
    def get_success_url(self):
        return reverse_lazy('login')


@login_required
def profile(request):
    data = Post.objects.filter(author = request.user)
    return render(request, 'profile.html', {'data': data})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ChangeUserData(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile Updated Successfully ')
            return redirect('profile')
        
    else:
        form = ChangeUserData(instance = request.user)
    return render(request, 'edit_profile.html', {'form': form})



@login_required
def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, data = request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Password Updated successful')
            update_session_auth_hash(request, form.user)
            return redirect('profile')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'pass_change.html', {'form': form})

