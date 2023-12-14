from django.shortcuts import render, redirect
from .forms import *

# Create your views here.
def musician_add(request):
    if request.method == "POST":
        musician_from = MusicianFrom(request.POST)
        if musician_from.is_valid():
            musician_from.save()
            print(musician_from.cleaned_data)
            return redirect('home')
    else:
        musician_from = MusicianFrom()
    return render(request, 'musician_add.html', {'from': musician_from})

def musician_edit(request, id):
    musician = Musician.objects.get(pk=id)
    musician_from = MusicianFrom( instance = musician)
    if request.method == "POST":
        musician_from = MusicianFrom(request.POST, instance = musician)
        if musician_from.is_valid():
            musician_from.save()
            return redirect('home')

    return render(request, 'musician_edit.html', {'from': musician_from})