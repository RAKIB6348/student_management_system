from django.urls import path
from accounts_users.views import *

urlpatterns = [
    # login urls
    path('', login_page, name='login_page'),
    path('login/', user_login, name="user_login"),

    #dashboard urls
    path('dashboard/', dashboard_page, name='dashboard_page'),

    path('home/admin/', admin_home_page, name='admin_home_page'),
]
