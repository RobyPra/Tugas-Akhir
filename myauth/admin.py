from django.contrib import admin
from .models import *
from import_export.admin import ExportActionMixin 
# Register your models here.

#admin.site.register(Employee)
@admin.register(Employee)
class EmployeeAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'phone','email')
    search_fields = ("first_name__startswith", )