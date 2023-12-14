from django import forms
from .models import TaskModel

class TaskFrom(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = ['task_title', 'task_description', 'category']
        
        # widgets = {
        #     'category': forms.MultipleChoiceField()
        # }

class TaskEditFrom(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = ['task_title', 'task_description', 'category', 'is_completed']