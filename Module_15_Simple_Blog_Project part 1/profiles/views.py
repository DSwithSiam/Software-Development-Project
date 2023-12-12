from django.shortcuts import render, redirect
from .forms import *

# Create your views here.
def add_profile(request):
    if request.method == 'POST':
        form = ProfileForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_profile')
    else:
        form = ProfileForms()
    return render(request, 'add_profile.html', {'form': form})