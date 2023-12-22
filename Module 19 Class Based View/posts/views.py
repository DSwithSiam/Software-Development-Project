from typing import Any
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .forms import *
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

# Create your views here.
# @login_required
# def add_post(request):
#     if request.method == 'POST':
#         form = PostForms(request.POST)
#         if form.is_valid():
#             # form.changed_data['author'] = request.user
#             form.instance.author = request.user
#             form.save()
#             return redirect('add_post')
#     else:
#         form = PostForms()
#     return render(request, 'add_post.html', {'form': form})

# useing class base view

class AddPostCreateView(CreateView):  
    model = Post
    form_class = PostForms
    template_name = 'add_post.html'
    success_url = reverse_lazy('add_post')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
     

# @login_required
# def edit_post(request, id):
#     post = Post.objects.get(pk=id)
#     form = PostForms(instance = post)
#     if request.method == 'POST':
#         form = PostForms(request.POST, instance = post)
#         if form.is_valid():
#             form.instance.author = request.user
#             form.save()
#             return redirect('profile')
    
#     return render(request, 'edit_post.html', {'form': form})

class EditPostView(UpdateView):
    model = Post
    form_class = PostForms
    template_name = 'edit_post.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('profile')
    

# @login_required
# def delete_post(request, id):
#     post = Post.objects.get(pk=id).delete()  # / post.delete()
#     return redirect('home_page')

class DeletePostView(DeleteView):
    model = Post
    pk_url_kwarg = 'id'
    template_name = 'delete.html'
    success_url = reverse_lazy('profile')
    
class DetailsPostView(DetailView):
    model = Post
    pk_url_kwarg = 'id'
    template_name = 'post_details.html'
    
    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(data = self.request.POST)
        post = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
        return self.get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs: Any):
        context =  super().get_context_data(**kwargs)
        post = self.object # post model er object ekhane store korlam 
        comments = post.comment.all()
        comment_form = CommentForm()
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context