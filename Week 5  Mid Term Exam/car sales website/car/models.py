from django.db import models

# Create your models here.

class BrandModel(models.Model):
    brand_name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=100, unique = True , null = True, blank=True)
    
    def __str__(self):
        return self.brand_name

class CarModel(models.Model):
    car_image = models.ImageField(upload_to='car/' ,verbose_name = 'image')
    car_name = models.CharField(max_length=30)
    car_price = models.IntegerField(default=0)
    car_quantity = models.IntegerField(default=0, blank=True, null = True)
    car_decription = models.CharField(max_length=200, blank=True, null = True)
    car_brand = models.ForeignKey(BrandModel, on_delete = models.CASCADE )
    
    
    def __str__(self):
        return self.car_name
    
class CommentModel(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=30)
    comment = models.TextField()
    post = models.ForeignKey(CarModel, on_delete=models.CASCADE)

