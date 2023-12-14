from django.urls import path, include
from .views import *

urlpatterns = [
    path('add/', task_add, name = 'task_add'),
    path('view/', tasks_view, name = 'tasks_view'),
    path('task/<int:id>', task_delete, name = 'task_delete'),
    path('edit/<int:id>', task_edit, name = 'task_edit'),
]
    