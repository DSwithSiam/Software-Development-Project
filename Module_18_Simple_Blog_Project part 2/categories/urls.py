from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('add/', add_categories, name='add_categories')
]
