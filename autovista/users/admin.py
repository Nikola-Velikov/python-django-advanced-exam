from django.contrib import admin
from django.contrib.auth import get_user_model
from django.core.exceptions import PermissionDenied
from .models import AppUser

@admin.register(AppUser)
class AppUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    search_fields = ('email', 'username')
    ordering = ('-is_staff',)

    fieldsets = (
        ("User Details", {
            'fields': ('email', 'username', 'is_staff', 'is_active'),
        }),
    )

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.is_superuser:
            return queryset  # Allow superusers to see all users
        return queryset.filter(is_staff=False)  # Restrict non-superusers to only view non-staff users

    def save_model(self, request, obj, form, change):
        # Allow only superusers to modify user details
        if not request.user.is_superuser:
            raise PermissionDenied("Only superusers can modify user details.")
        super().save_model(request, obj, form, change)

    def has_change_permission(self, request, obj=None):
        # Allow only superusers to modify users
        return request.user.is_superuser
