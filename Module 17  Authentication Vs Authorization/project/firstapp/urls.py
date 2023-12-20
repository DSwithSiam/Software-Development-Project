from django.urls import path
from . views  import *

urlpatterns = [
    path('signin/', signin, name = 'signin'),
    path('login/', user_login, name = 'login'),
    path('logout/', user_logout, name = 'logout'),
    path('pass_change/', pass_change, name = 'pass_change'),
    path('pass_change2/', pass_change2, name = 'pass_change2'),
    path('profile/', profile, name = 'profile'),
]
