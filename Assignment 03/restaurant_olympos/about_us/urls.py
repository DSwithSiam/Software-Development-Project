
from django.urls import path
from .views import *

urlpatterns = [
    path('' , about_us, name = 'about_us')
]
