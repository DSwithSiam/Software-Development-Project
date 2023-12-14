from django.shortcuts import render, redirect
from .forms import *

# Create your views here.
def HomePage(request):
    if request.method == "POST":
        form = ExampleForm(request.POST)
        if form.is_valid():
            print (form.cleaned_data)
            return redirect('home')
    else:
        form = ExampleForm()
    return render(request, 'home.html', {'form': form})	


def model(request):
    if request.method == "POST":
        form = ModelForm(request.POST)
        if form.is_valid():
            print (form.cleaned_data)
            form.save()
            return redirect('home')
    else:
        form = ModelForm()
    return render(request, 'model.html', {'model_form': form})	