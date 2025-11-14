from django.shortcuts import render

# Create your views here.
def dashboard_page(request):

    return render(request, 'dashboard.html')



def login_page(request):

    return render(request, 'login.html')



