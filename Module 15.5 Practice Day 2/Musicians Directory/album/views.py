from django.shortcuts import render, redirect
from .forms import *
from musician.urls import *
from .models import *
# Create your views here.

def album_add(request):
    if request.method == "POST":
        album_from = AlbumFrom(request.POST)
        if album_from.is_valid():
            album_from.save()
            print(album_from.cleaned_data)
            return redirect('home')
    else:
        album_from = AlbumFrom()
    return render(request, 'album_add.html', {'from': album_from})

def album_delete(request, id):
    album =  Album.objects.get(pk=id).delete()
    return redirect('home')

def album_edit(request, id):
    album = Album.objects.get(pk=id)
    album_from = AlbumFrom( instance = album)
    if request.method == "POST":
        album_from = AlbumFrom(request.POST, instance = album)
        if album_from.is_valid():
            album_from.save()
            return redirect('home')

    return render(request, 'album_edit.html', {'from': album_from})