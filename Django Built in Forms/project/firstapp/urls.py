from django.urls import path
from . views  import *

urlpatterns = [
    path('', HomePage, name="home"),
    path('django_form/', DjangoForm, name="django_form"),
    path('student_form/', StudentForm, name="student_form"),
    path('password_validation/', PasswordValidation, name="password_validation"),
]
