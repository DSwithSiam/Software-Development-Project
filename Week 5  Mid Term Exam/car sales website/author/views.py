from django.shortcuts import render, redirect
from author.models import AddCardModel
from car.models import CarModel
from .forms import *
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.
@login_required(login_url='user_login')
def profile(request):
    card = AddCardModel.objects.all()
    user_data = request.user
    return render(request, 'profile.html', {'user_data': user_data, 'card': card,})


def user_register(request):
    if request.method == 'POST':
        form = RegisterFrom(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful")
            return redirect('user_login')
    else:
        form = RegisterFrom()
    return render(request, 'signup.html', {'form': form})


class user_login(LoginView):
    model = User
    template_name = 'login.html'
    def get_success_url(self):
        return reverse_lazy('profile')
    
    def form_valid(self, form):
        messages.success(self.request, 'Login successful')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.success(self.request, 'Logged in information incorrect')
        return super().form_invalid(form)
    
@method_decorator(login_required(login_url='user_login'), name='dispatch')
class user_logout(LogoutView):
    def get_success_url(self):
        return reverse_lazy('user_login')

@method_decorator(login_required(login_url='user_login'), name='dispatch')
class edit_profile(UpdateView):
    model = User
    form_class = UserChangeForm
    pk_url_kwarg = 'pk'
    template_name = 'edit_profile.html'
    def get_success_url(self):
        return reverse_lazy('profile')
            