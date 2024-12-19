from django.contrib import admin
from django.core.exceptions import PermissionDenied

from .models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    list_filter = ('created_at', 'subject')
    search_fields = ('name', 'email', 'subject', 'message')
    ordering = ('-created_at',)

    fieldsets = (
        ("Message Details", {
            'fields': ('name', 'email', 'subject', 'message'),
        }),
    )



    def save_model(self, request, obj, form, change):
        # Restrict staff users from modifying certain fields if needed
        if request.user.groups.filter(name="Staff").exists():
            if 'message' in form.changed_data:
                raise PermissionDenied("Staff users cannot modify the message content!")
        super().save_model(request, obj, form, change)
