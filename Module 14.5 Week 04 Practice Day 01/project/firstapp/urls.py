from django.urls import path
from .views  import *

urlpatterns = [
    path('', HomePage, name="home"),
    path('model/', model, name="model"),
]
