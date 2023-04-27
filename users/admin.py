from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import RegistrationForm, UpdateForm

from .models import MyUser, StaffProfile, GisStaffProfile


class CustomAdmin(UserAdmin):
    add_form = RegistrationForm
    form = UpdateForm
    model = MyUser

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
        ("permissions", {"fields": ("is_active", "is_staff", "is_admin")}),
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
                    "password1",
                    "password2",
                ),
            },
        ),
    )


admin.site.register(StaffProfile)
admin.site.register(GisStaffProfile)
admin.site.register(MyUser, CustomAdmin)
