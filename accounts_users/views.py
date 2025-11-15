from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages




# Create your views here.
def dashboard_page(request):

    return render(request, 'dashboard.html')



def login_page(request):

    return render(request, 'login.html')



def user_login(request):
    if request.method == 'POST':

        user_id = request.POST.get('user_id')
        password = request.POST.get('password')

        user = authenticate(request, username=user_id, password=password)
        print("AUTH RESULT:", user) 

        if user:
            login(request, user)
            
            user_type = user.user_type
            print('USER TYPE ----------', user_type)

            # admin type
            if user_type == 'Admin':
                return HttpResponse("This is a Admin panel dashboard")

            elif user_type == 'Teacher':
                return HttpResponse("This is a Teacher panel dashboard")

            elif user_type == 'Student':
                return HttpResponse("This is a Student panel dashboard")

            else:
                messages.error(request, "User type is not valid!")
                return redirect('login_page')   
        messages.error(request, "Invalid User ID or Password.")     
        return redirect('login_page')

    return redirect('login_page')