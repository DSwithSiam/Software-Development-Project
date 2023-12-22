from django.urls import path
from . views  import *

urlpatterns = [
    # path('', HomePage, name="home"),
    # path('get/', get_cookies, name="get"),
    # path('del/', del_cookies, name="del"),
    path('', set_session, name="home"),
    path('get/', get_session, name="get"),
    path('del/', del_session, name="del"),
]
