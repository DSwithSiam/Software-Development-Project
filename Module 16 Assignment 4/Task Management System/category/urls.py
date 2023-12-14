from django.urls import path, include
from .views import *

urlpatterns = [
    path('add/', category_add, name = 'category_add')
]
    