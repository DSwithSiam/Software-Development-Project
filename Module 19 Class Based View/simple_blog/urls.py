from django.contrib import admin
from django.urls import path, include
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePage, name = 'home_page'),
    path('category/<slug:category_slug>/', HomePage, name = 'category_post'),
    path('author/', include('author.urls')),
    path('post/', include('posts.urls')),
    path('categorie/', include('categories.urls')),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
