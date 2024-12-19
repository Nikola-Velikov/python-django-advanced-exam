from django import forms

from .models import Offer


class BaseOfferForm(forms.ModelForm):
    class Meta:
        model = Offer
        exclude = ['updated_at', 'owner', 'created_at']


class CreateOffer(BaseOfferForm):
    pass


class UpdateOffer(BaseOfferForm):
    pass


class DeleteOfferForm(BaseOfferForm):
    pass
