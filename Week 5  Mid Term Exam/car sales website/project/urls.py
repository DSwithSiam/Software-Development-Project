from django.contrib import admin
from django.urls import path, include
from project import settings
from .views import HomePage
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePage, name='home'),
    path('car/<slug:post_slug>', HomePage, name='post_filter'),
    path('car/', include('car.urls')),
    path('author/', include('author.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)