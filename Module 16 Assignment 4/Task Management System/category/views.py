from django.shortcuts import render, redirect
from .forms import *
from .models import *
# Create your views here.

def category_add(request):
    if request.method == "POST":
        category_from = CategoryFrom(request.POST)
        if category_from.is_valid():
            category_from.save()
            print(category_from.cleaned_data)
            return redirect('home')
    else:
        category_from = CategoryFrom()
    return render(request, 'category_add.html', {'from': category_from})