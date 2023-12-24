from django.db import models
from musician.models import *

# Create your models here.
class Album(models.Model):
    name = models.CharField(max_length=100)
    musician = models.ForeignKey(Musician, on_delete= models.CASCADE )
    release_date = models.DateField(auto_now_add=True)
    RATING_CHOICES = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4,  4),
        (5, 5),
        ]
    rating = models.IntegerField(choices = RATING_CHOICES)
    
    def __str__(self):
        return self.name