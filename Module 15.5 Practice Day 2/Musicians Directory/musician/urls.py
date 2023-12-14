from django.urls import path
from . views  import *

urlpatterns = [
    
    path('add/', musician_add, name="musician_add"),
    path('edit/<int:id>', musician_edit, name="musician_edit"),
]
