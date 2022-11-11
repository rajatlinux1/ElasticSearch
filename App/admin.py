from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import UserData
# Register your models here.
@admin.register(UserData)
class UserDataAdmin(ImportExportModelAdmin):
    list_display=['id','name','city','email','profile_pic']
