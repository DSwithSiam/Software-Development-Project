from typing import Any
from django import forms
from django.core import validators

# widgets --> fiels to html input
class ContactForm(forms.Form):
    # name = forms.CharField(label = 'User name', initial="Siam", help_text="Enter your name", required=False, disabled=True)
    # file = forms.FileField()
    # email = forms.EmailField(label = 'User email')
    # age = forms.IntegerField(label = 'Age')
    # weight = forms.FloatField(label = 'Weight')
    # balance = forms.DecimalField(label = 'Balance')
    # check = forms.BooleanField(label = 'Check')
    # birthday = forms.DateField(label = 'Birthday')
    # appointment = forms.DateTimeField(label = 'Appointment')
    # CHOICES = [('S', 'Small'), ('M', 'Medium'), ('L', 'Large')]
    # size = forms.ChoiceField(choices = CHOICES)
    # MEAL = [('P', 'Pepperoni'), ('M', 'Mashroom'), ('B', 'Beef')]
    # pizza = forms.MultipleChoiceField(choices = MEAL)
    
    name = forms.CharField(label = 'User name', initial="Siam", help_text="Enter your name", required=False, disabled=True)
    file = forms.FileField(required=False)
    email = forms.EmailField(label = 'User email')
    age = forms.IntegerField(label = 'Age', widget=forms.NumberInput)
    weight = forms.FloatField(label = 'Weight')
    balance = forms.DecimalField(label = 'Balance')
    check = forms.BooleanField(label = 'Check')
    birthday = forms.DateField(label = 'Birthday', widget= forms.DateInput(attrs = {'type': 'date'}))
    appointment = forms.DateTimeField(label = 'Appointment', widget= forms.DateInput(attrs = {'type': 'datetime-local'}))
    CHOICES = [('S', 'Small'), ('M', 'Medium'), ('L', 'Large')]
    size = forms.ChoiceField(choices = CHOICES, widget= forms.RadioSelect)
    MEAL = [('P', 'Pepperoni'), ('M', 'Mashroom'), ('B', 'Beef')]
    pizza = forms.MultipleChoiceField(choices = MEAL, widget= forms.CheckboxSelectMultiple)
    textbox = forms.CharField(required=False, widget=forms.Textarea)
                               

# class StudentData(forms.Form):
#     name = forms.CharField()
#     email = forms.EmailField()
    
    # def clean_name(self):
    #     valname = self.cleaned_data['name']
    #     if len(valname) < 10:
    #         raise forms.ValidationError("Enter a name with at last 10 characters")
        
    #     return valname
    
    # def clean_email(self):
    #     valname = self.cleaned_data['email']
    #     if '.com' not in valname:
    #         raise forms.ValidationError("Your email must contain .com and a valid email address")
    #     return valname
    
    # def clean(self):
    #     cleaned_data = super().clean()
    #     valname = self.cleaned_data['name']
    #     valemail = self.cleaned_data['email']
    #     if len(valname) < 10:
    #         raise forms.ValidationError("Enter a name with at last 10 characters")
    #     if '.com' not in valemail:
    #         raise forms.ValidationError("Your email must contain .com and a valid email address")

def len_check(value):
    if len(value) < 10:
        raise forms.ValidationError("Enter a value at last 10 characters")

class StudentData(forms.Form):
    name = forms.CharField(validators=[validators.MinLengthValidator(10, message='Enter a name with at last 10 characters')])
    email = forms.EmailField(validators=[validators.EmailValidator(message='Enter a valid email address')])
    age = forms.IntegerField(validators=[validators.MaxValueValidator(35, message='Age must be maximum of 35 '), validators.MinValueValidator(18, message='Age must be at least 18')])
    file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['png'], message='File extension must be .png')])
    text = forms.CharField(widget=forms.Textarea, validators=[len_check])
    # Regex, url -> diye korte pari aro
    
class Password_validation_from(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    
    def clean(self):
        cleaned_data  = super().clean()
        val_pass = self.cleaned_data['password']
        val_conpass = self.cleaned_data['confirm_password']
        
        if val_pass != val_conpass:
            raise forms.ValidationError('Passwords do not match')
        if '@' not in val_pass and '#' not in val_pass:
            raise forms.ValidationError('Type Stored password') 