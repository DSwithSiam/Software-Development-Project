from django.urls import path
from . views  import *

urlpatterns = [
    path('profile/', profile, name='profile'),
    path('register/', user_register, name='user_register'),
    path('login/', user_login.as_view(), name='user_login'),
    path('logout/', user_logout.as_view(), name='user_logout'),
    path('edit/<int:pk>', edit_profile.as_view(), name='edit_profile'),
    
]
