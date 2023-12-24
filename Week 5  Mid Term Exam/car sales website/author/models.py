from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class AddCardModel(models.Model):
    car_card_pk = models.IntegerField(blank=True, null = True)
    car_image = models.ImageField(upload_to='car/' ,verbose_name = 'image')
    car_name = models.CharField(max_length=30)
    car_price = models.IntegerField(default=0)
    car_quantity = models.IntegerField(default=0, blank=True, null = True)
    car_decription = models.CharField(max_length=200, blank=True, null = True)
    car_brand = models.CharField(max_length=200)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)