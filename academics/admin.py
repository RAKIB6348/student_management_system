from django.contrib import admin
from academics.models import *

# Register your models here.
class StudentClassAdmin(admin.ModelAdmin):

	list_display = ['name','code']

	search_fields = ['name','code']


admin.site.register(StudentClass, StudentClassAdmin)
