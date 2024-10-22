from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomerUserCreationForm, CustomUserChangeForm
from .models import CustomUser

# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomerUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    list_display = [
        "email",
        "username", 
        "firstname", #new field
        "lastname",
        "age",
        "is_staff",
        "about",
        "classes",
        "weekDayAvailable",
        "hourAvailable", # new
        
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields":
        ("age", "firstname", "lastname")}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields":
        ("age", "firstname", "lastname")}),)
    
admin.site.register(CustomUser, CustomUserAdmin)
