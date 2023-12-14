from django.urls import path
from . views  import *

urlpatterns = [
    path('add/', album_add, name="album_add"),
    path('delete/<int:id>', album_delete, name="album_delete"),
    path('edit/<int:id>', album_edit, name="album_edit"),
]
