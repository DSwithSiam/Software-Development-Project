from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePage, name = 'home_page'),
    path('category/<slug:category_slug>/', HomePage, name = 'category_post'),
    path('author/', include('author.urls')),
    path('post/', include('posts.urls')),
    path('categorie/', include('categories.urls')),
    
]
