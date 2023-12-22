from django.urls import path
from . views  import *

urlpatterns = [
    path('register/', user_register, name = 'user_register'),
    path('profile/', profile, name = 'profile'),
    path('login/', user_login, name = 'user_login'),
    path('logout/', user_logout, name = 'user_logout'),
    path('pass_change/', pass_change, name = 'pass_change'),
    
]
