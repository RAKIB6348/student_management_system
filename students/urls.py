from django.urls import path
from students.views import *

urlpatterns = [
	path('student-list/', student_list, name="student_list"),
	path('student-add/', student_add, name="student_add"),
]