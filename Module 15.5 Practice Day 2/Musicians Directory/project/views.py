from django.shortcuts import render
from album.models import Album

# Create your views here.
def HomePage(request):
    album_data = Album.objects.all()
    print(album_data)
    return render(request, 'home.html', {'album_data': album_data})