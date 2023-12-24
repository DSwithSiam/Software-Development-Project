from django.shortcuts import render, redirect
from car.models import *
from car.forms import *

# Create your views here.
def HomePage(request, post_slug = None):
    data = CarModel.objects.all()
    brands = BrandModel.objects.all()
    if post_slug is not None:
        brand = BrandModel.objects.filter(slug = post_slug).first()
        data = CarModel.objects.filter(car_brand = brand)
    
    return render(request, 'home.html', {'data': data, 'brand': brands})