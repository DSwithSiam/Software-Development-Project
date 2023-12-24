from django.shortcuts import render, redirect
from .forms import *
from django.views.generic import CreateView,  DeleteView, UpdateView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.

@method_decorator(login_required, name='dispatch')
class musician_add_class(CreateView):
    model = Musician
    form_class = MusicianFrom
    template_name = 'musician_add.html'
    success_url = reverse_lazy('home')


@method_decorator(login_required, name='dispatch')
class musician_edit_class(UpdateView):
    model = Musician
    form_class = MusicianFrom
    template_name = 'musician_edit.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home')
    