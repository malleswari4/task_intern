from django.contrib import admin
from App.models import *
# Register your models here.
@admin.register(User_Register)
class UserAdmin(admin.ModelAdmin):
    list_display=('id','reg_name','reg_email','reg_address','reg_pass')
