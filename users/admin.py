from typing import Optional
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model
from django.http.request import HttpRequest
from .forms import RegistrationForm, UpdateForm

from . import models



class UserAdminArea(admin.AdminSite):
    site_header = "FEDERAL MINISTRY OF ENVIRONMENT/EAD"
    


class TestAdminPermissions(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        
        if request.user.groups.filter(name='Administrator').exists():
            return False
        
        return obj

    def has_change_permission(self, request, obj=None):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False
    
    def has_view_permission(self, request, obj=None):
        return True
    
    
    
    
    
user_site = UserAdminArea(name= 'User Management')


user_site.register(models.MyUser, TestAdminPermissions)
user_site.register(models.Profile)





class CustomAdmin(BaseUserAdmin):
    add_form = RegistrationForm
    form = UpdateForm
    model = models.MyUser

    search_fields = ("email", "username", "staff_id")
    list_filter = ("email", "username", "is_active", "is_staff", "is_admin")
    ordering = ("-sign_up_date",)
    list_display = (
        "email",
        "username",
        "is_active",
        "is_admin",
        "is_staff",
        "is_superuser",
    )
    fieldsets = (
        (None, {"fields": ("email", "username", "staff_id", "password")}),
        ("permissions", {"fields": ("is_active", "is_staff", "is_admin", "is_superuser", "groups")}),
        ("personal", {"fields": ()}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "username",
                    "staff_id",
                    "is_active",
                    "is_staff",
                    "is_admin",
                    "is_superuser",
                    "group",
                    "password1",
                    "password2",
                ),
            },
        ),
    )
admin.site.register(models.MyUser, CustomAdmin)
admin.site.register(models.Profile)