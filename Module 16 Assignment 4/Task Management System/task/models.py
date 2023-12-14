from django.db import models
from category.models import TaskCategoryModel

# Create your models here.
class TaskModel(models.Model):
    task_title = models.CharField(max_length=100)
    task_description = models.TextField()
    category = models.ManyToManyField(TaskCategoryModel)
    task_assign_date = models.DateField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.task_title
    
    