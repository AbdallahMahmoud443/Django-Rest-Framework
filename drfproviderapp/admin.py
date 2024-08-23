from django.contrib import admin

from drfproviderapp.models import Countries, Departments, Employee

# Register your models here.

admin.site.register(Employee)
admin.site.register(Departments)
admin.site.register(Countries)