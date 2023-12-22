from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('register/', register_user, name = 'register'), 
    # path('login/', user_login, name = 'login'), 
    path('login/', userLoginView.as_view(), name = 'login'), 
    # path('logout/', user_logout, name = 'logout'), 
    path('logout/', UserLogoutView.as_view(), name = 'logout'), 
    path('profile/', profile, name = 'profile'), 
    path('profile/edit', edit_profile, name = 'edit_profile'), 
    path('password_change/', password_change, name = 'password_change'), 
    
]
