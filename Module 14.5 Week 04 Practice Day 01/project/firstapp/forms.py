from django import forms
import datetime
from django.forms.widgets import NumberInput
from .models import MyModel


class ExampleForm(forms.Form):
    name = forms.CharField()
    first_name = forms.CharField(initial='Your name')
    # comment = forms.CharField(widget=forms.Textarea)
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    email = forms.EmailField()
    agree = forms.BooleanField()
    agree = forms.BooleanField(initial=True)
    date = forms.DateField()
    birth_date = forms.DateField(widget = NumberInput(attrs={'type': 'date'}))
    day = forms.DateField(initial=datetime.date.today)
    BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years= BIRTH_YEAR_CHOICES))
    value = forms.DecimalField()
    email_address = forms.EmailField( required = False,)
    message = forms.CharField( max_length = 10, )
    email_address = forms.EmailField( label="Please enter your email address", )
    
    FAVORITE_COLORS_CHOICES = [('blue', 'Blue'),('green', 'Green'),('black', 'Black')]
    favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)
    favorite_color = forms.ChoiceField(widget=forms.RadioSelect, choices=FAVORITE_COLORS_CHOICES)
    favorite_colors = forms.MultipleChoiceField(choices=FAVORITE_COLORS_CHOICES)
    favorite_colors = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=FAVORITE_COLORS_CHOICES)
    
    
    password = forms.CharField(widget = forms.PasswordInput()) 
    roll_number = forms.IntegerField(help_text = "Enter 6 digit roll number") 

class ModelForm(forms.ModelForm):
    
    class Meta:
        model = MyModel
        fields = '__all__'

    