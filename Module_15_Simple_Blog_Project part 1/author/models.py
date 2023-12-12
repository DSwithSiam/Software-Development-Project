from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=12)
    bio = models.TextField()
    
    def __str__(self):
        return f"Name: {self.name}"
    