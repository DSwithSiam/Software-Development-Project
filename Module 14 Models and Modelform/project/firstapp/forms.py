from django import forms
from firstapp.models import *

class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        labels = {
            'name': 'Student Name',
            'roll': 'Student Roll',
        }
        # widgets = {
        #     'name': forms.TextInput(attrs={'class': ''}),
        #     'roll': forms.PasswordInput()
        # }        
        # help_texts = {
        #     'name': 'Write your full name',
        #     'roll': 'Enter Strong Password'           
        # }
        # error_massages = {
        #     'name': 'Your Name is Required',
        # }