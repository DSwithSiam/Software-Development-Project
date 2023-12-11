from django.shortcuts import render, redirect
from firstapp.forms import StudentModelForm
from . import models


# Create your views here.
def HomePage(request):
    students = models.Student.objects.all()
    
    return render(request, 'home.html', {'students': students})


def DeleteStudent(request, roll):
    students = models.Student.objects.get(pk = roll).delete()
    
    return redirect('home')

def StudentFromSubmission(request):
    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            # commit=False
            form.save()
            print(form.cleaned_data)
    
    else:
        form = StudentModelForm()
    return render(request, 'student_from.html', {'form': form})
    