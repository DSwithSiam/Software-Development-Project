from django.shortcuts import render, redirect
from .forms import *

# Create your views here.
def add_author(request):
    if request.method == 'POST':
        form = AuthorForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_author')
    else:
        form = AuthorForms()
    return render(request, 'add_author.html', {'form': form})