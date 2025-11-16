from django.shortcuts import render

# Create your views here.
def student_list(request):

	return render(request, 'student/student_list.html')



def student_add(request):

	return render(request, 'student/add_student.html')
