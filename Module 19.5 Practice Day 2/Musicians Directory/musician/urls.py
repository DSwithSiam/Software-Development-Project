from django.urls import path
from . views  import *

urlpatterns = [
    
    path('add/', musician_add_class.as_view(), name="musician_add"),
    path('edit/<int:id>', musician_edit_class.as_view(), name="musician_edit"),
]
