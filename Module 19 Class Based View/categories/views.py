from django.shortcuts import render, redirect
from .forms import *

# Create your views here.
def add_categories(request):
    if request.method == 'POST':
        form = CategoriesForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_categories')
    else:
        form = CategoriesForms()
    return render(request, 'add_categories.html', {'form': form})