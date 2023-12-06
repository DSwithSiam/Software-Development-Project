from django.urls import path
from . views import *

urlpatterns = [
    path('',  Homepage, name = 'home')
    
]
