from django.shortcuts import render

# Create your views here.
def About(request):
    return render(request, 'firstapp/About.html')

def Contact_us(request):
    return render(request, 'firstapp/contact_us.html')

def Services(request):
    return render(request, 'firstapp/services.html')