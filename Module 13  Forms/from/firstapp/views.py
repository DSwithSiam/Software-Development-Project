from django.shortcuts import render

# Create your views here.
def home(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        return render(request, 'home.html', {'email': email, 'password': password})
    return render(request, 'home.html')