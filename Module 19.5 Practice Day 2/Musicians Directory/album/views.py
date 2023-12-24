from django.shortcuts import render, redirect
from .forms import *
from musician.urls import *
from .models import *
from django.views.generic import CreateView,  DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

# Create your views here.


@method_decorator(login_required, name='dispatch')
class album_add_class(CreateView):
    model = Album
    form_class = AlbumFrom
    template_name = 'album_add.html'
    success_url = reverse_lazy('home')


@method_decorator(login_required, name='dispatch')
class album_delete_class(DeleteView):
    model = Album
    pk_url_kwarg = 'id'
    template_name = "album_confirm_delete.html"
    success_url = reverse_lazy('home')

@method_decorator(login_required, name='dispatch')
class album_edit_class(UpdateView):
    model = Album
    form_class = AlbumFrom
    pk_url_kwarg = 'id'
    template_name = 'album_edit.html'
    success_url = reverse_lazy('home')
    
