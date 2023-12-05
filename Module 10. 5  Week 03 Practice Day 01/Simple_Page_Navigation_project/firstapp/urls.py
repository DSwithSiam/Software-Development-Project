from django.urls import path
from .views import *

urlpatterns = [
    path('about/',  About),
    path('contact_us/' , Contact_us),
    path('services/' , Services),
]