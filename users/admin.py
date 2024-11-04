from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Position

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'full_name', 'position', 'dismissed', 'dismissal_date', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('full_name', 'position', 'dismissed', 'dismissal_date')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Position)
