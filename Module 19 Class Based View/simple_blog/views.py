from django.shortcuts import render
from posts.models import Post
from categories.models import Category

def HomePage(request, category_slug = None):
    data = Post.objects.all()
    categories = Category.objects.all()
    if category_slug is not None:
        category = Category.objects.get(slug = category_slug)
        data = Post.objects.filter(category = category)
    return render(request, 'home.html', {'data': data, 'category': categories})	