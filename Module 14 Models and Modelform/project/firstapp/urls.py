from django.urls import path
from . views  import *

urlpatterns = [
    path('', HomePage, name="home"),
    path('delete/<int:roll>', DeleteStudent, name="delete_student"),
    path('student_from', StudentFromSubmission, name="student_from"),
]
