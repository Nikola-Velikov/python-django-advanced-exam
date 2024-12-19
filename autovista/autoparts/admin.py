from django.contrib import admin
from django.core.exceptions import PermissionDenied

from .models import AutoPart


@admin.register(AutoPart)
class AutoPartAdmin(admin.ModelAdmin):
    list_display = ('title', 'model', 'price', 'owner', 'discounted_price')
    list_filter = ('model', 'price', 'owner')
    search_fields = ('title', 'model', 'owner__username')
    ordering = ('-price',)

    fieldsets = (
        ("Auto Part Details", {
            'fields': ('title', 'short_description', 'model', 'price', 'discounted_price', 'image', 'owner'),
        }),
    )

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.groups.filter(name="Staff").exists():
            # Restrict Staff users to their own auto parts
            return queryset.filter(owner=request.user)
        return queryset

