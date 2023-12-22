from django import forms
from .models import Category

class CategoriesForms(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        # fields = ['name']