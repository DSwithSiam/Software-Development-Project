from django.urls import path
from . views  import *

urlpatterns = [
    path("details/<int:pk>", CarDetails, name='car_details'),
    path("bay/<int:id>", bay_now, name='bay_now'),
]
