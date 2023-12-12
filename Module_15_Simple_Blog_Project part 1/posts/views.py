from django.shortcuts import render, redirect
from .forms import *

# Create your views here.
def add_post(request):
    if request.method == 'POST':
        form = PostForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_post')
    else:
        form = PostForms()
    return render(request, 'add_post.html', {'form': form})

def edit_post(request, id):
    post = Post.objects.get(pk=id)
    form = PostForms(instance = post)
    if request.method == 'POST':
        form = PostForms(request.POST, instance = post)
        if form.is_valid():
            form.save()
            return redirect('home_page')
    
    return render(request, 'edit_post.html', {'form': form})

def delete_post(request, id):
    post = Post.objects.get(pk=id).delete()  # / post.delete()
    
    return redirect('home_page')