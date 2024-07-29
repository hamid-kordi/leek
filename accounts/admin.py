from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


# Register your models here.
class UserAdmin(BaseUserAdmin):
    list_display = ("id","email", "phone_number", "is_admin", "is_superuser", "is_seller")
    list_filter = ("is_admin",)
    readonly_fields = ("last_login",)
    fieldsets = (
        ("Main", {"fields": ("email", "phone_number", "name", "password","user_name","is_seller")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_admin",
                    "is_superuser",
                    "last_login",
                    "groups",
                    "user_permissions",
                )
            },
        ),
    )

    add_fieldsets = (
        (
            None,
            {
                "fields": (
                    "phone_number",
                    "email",
                    "name",
                    "password1",
                    "password2",
                )
            },
        ),
    )

    search_fields = ("email", "name")
    ordering = ("name",)
    filter_horizontal = ("groups", "user_permissions")


admin.site.register(User, UserAdmin)
