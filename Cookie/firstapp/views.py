from datetime import datetime, timedelta
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def HomePage(request):
    response = render(request, 'home.html')
    # response.set_cookie('name', 'Rahim')
    # response.set_cookie('name', 'Rahim', max_age=60)
    response.set_cookie('name', 'Rahim', expires=datetime.utcnow()+timedelta(days=5))
    
    return response

def get_cookies(request):
    name = request.COOKIES.get('name')
    print(request.COOKIES)
    return render(request, 'get_cookies.html', {'name': name})
    
def del_cookies(request):
    response = render(request, 'del_cookies.html')
    response.delete_cookie('name')
    return response

def set_session(request):
    data = {
        'name': 'Korim',
        'age': 23,
    }
    print(request.session.get_session_cookie_age())
    print(request.session.get_expiry_date())
    request.session.update(data)
    return render(request, 'home.html')
    
def get_session(request):
    if 'name' in request.session:
        name = request.session.get('name', 'no name')
        age = request.session.get('age')
        request.session.modified = True
        return render(request, 'get_session.html', {'name': name, 'age': age})
    else:
        return HttpResponse("Login again")
    
    
def del_session(request):
    # del request.session['name']
    request.session.flush()
    return render(request, 'del_session.html')