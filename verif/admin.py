from django.contrib import admin
from import_export.admin import ExportActionMixin  
from .models import *

@admin.register(Person)
class PersonAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('no_ktp', 'first_name', 'last_name', 'gender', 'phone', 
                    'address', 'description', 'img', 'last_modified')
    list_filter = ('last_modified', )
    search_fields = ("first_name__startswith", )

@admin.register(Vehicle)
class VehicleAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('owner','no_polisi', 'vehicle_Type', 'last_modified')
    list_filter = ('last_modified', )
    search_fields = ('no_polisi', )

@admin.register(Log)
class LogAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('id','face_log', 'euclidean', 'cosine', 'time', 'img')
    list_filter = ('time', )
    
@admin.register(LastFace)
class LastFaceAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('id','last_face', 'euclidean', 'cosine', 'time',)
    list_filter = ('time', )
    search_fields = ('lace_face', )