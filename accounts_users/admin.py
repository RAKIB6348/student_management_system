from django.contrib import admin
from accounts_users.models import *

# Register your models here.
class UserAdmin(admin.ModelAdmin):

    list_display = ['username', 'user_id', 'user_type', 'is_superuser', 'email']

    search_fields = ['username', 'user_id', 'email']



admin.site.register(User, UserAdmin)
