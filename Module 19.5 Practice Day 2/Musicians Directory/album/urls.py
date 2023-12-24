from django.urls import path
from . views  import *

urlpatterns = [
    path('add/', album_add_class.as_view(), name="album_add"),
    path('delete/<int:id>', album_delete_class.as_view(), name="album_delete"),
    path('edit/<int:id>', album_edit_class.as_view(), name="album_edit"),
]
