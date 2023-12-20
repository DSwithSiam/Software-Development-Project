from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import *

# Create your views here.
@login_required
def add_post(request):
    if request.method == 'POST':
        form = PostForms(request.POST)
        if form.is_valid():
            # form.changed_data['author'] = request.user
            form.instance.author = request.user
            form.save()
            return redirect('add_post')
    else:
        form = PostForms()
    return render(request, 'add_post.html', {'form': form})

@login_required
def edit_post(request, id):
    post = Post.objects.get(pk=id)
    form = PostForms(instance = post)
    if request.method == 'POST':
        form = PostForms(request.POST, instance = post)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            return redirect('home_page')
    
    return render(request, 'edit_post.html', {'form': form})

@login_required
def delete_post(request, id):
    post = Post.objects.get(pk=id).delete()  # / post.delete()
    
    return redirect('home_page')