from django.db import models

# Create your models here.
class Musician(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.IntegerField(max_length=12)
    instument_type = models.CharField(max_length=20)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"