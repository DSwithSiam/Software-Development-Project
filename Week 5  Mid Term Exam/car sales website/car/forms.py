from django import forms
from car.models import CarModel, BrandModel, CommentModel


class CarFrom(forms.ModelForm):
    class Meta:
        model = CarModel
        fields = '__all__'
        
class CarBrandForm(forms.ModelForm):
    class Meta:
        model = BrandModel
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ['name', 'email', 'comment',]