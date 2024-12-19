from django.contrib import admin
from django.core.exceptions import PermissionDenied

from .models import Offer

@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ('title', 'model', 'price', 'fuel', 'owner', 'discounted_price')

    list_filter = ('fuel', 'gearbox', 'doors', 'owner')

    search_fields = ('title', 'model', 'owner__username')

    ordering = ('-price',)

    readonly_fields = ('discounted_price',)

    fieldsets = (
        ("Vehicle Details", {
            'fields': ('type_used_vehicle', 'model', 'mileage', 'fuel', 'power', 'gearbox', 'number_of_seats', 'doors'),
        }),
        ("Offer Details", {
            'fields': ('title', 'image', 'short_description', 'price', 'discounted_price', 'owner'),
        }),
    )


    def save_model(self, request, obj, form, change):
        # Restrict staff users from modifying certain fields
        if request.user.groups.filter(name="Staff").exists():
            if 'price' in form.changed_data:
                raise PermissionDenied("Staff users cannot change the price!")
        super().save_model(request, obj, form, change)