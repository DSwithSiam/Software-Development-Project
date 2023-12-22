from django.contrib import admin
from django.urls import path, include
from .views import HomePage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('author/', include('profile.urls')),
    path('', HomePage, name= 'home'),
]
