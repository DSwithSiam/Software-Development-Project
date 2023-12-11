from django.shortcuts import render
from firstapp.forms import *

# Create your views here.
def HomePage(request):
    return render(request, 'home.html')
def DjangoForm(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            # uplode image save in uplode folder
            file = form.cleaned_data['file']
            if file:
                with open('./firstapp/upload/' + file.name, 'wb+' ) as destination:
                    for chunk in file.chunks():
                        destination.write(chunk)
            print(form.cleaned_data)
            
            return render(request, 'django_form.html', {'form': form})
    else:
        form = ContactForm()
    return render(request, 'django_form.html', {'form': form})


def StudentForm(request):
    if request.method == 'POST':
        form = StudentData(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            if file:
                with open('./firstapp/upload/' + file.name, 'wb+' ) as destination:
                    for chunk in file.chunks():
                        destination.write(chunk)
            print(form.cleaned_data)
            return render(request, 'django_form2.html', {'form': form})
    else:
        form = StudentData()
    return render(request, 'django_form2.html', {'form': form})

def PasswordValidation(request):
    if request.method == 'POST':
        form  = Password_validation_from(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
        return render(request, 'django_form3.html', {'form': form})
    else:
        form  = Password_validation_from()
    return render(request, 'django_form3.html', {'form': form})