from django import forms

from .models import AutoPart


class BaseAutoPartForm(forms.ModelForm):
    class Meta:
        model = AutoPart
        exclude = ['owner']


class CreateAutoPart(BaseAutoPartForm):
    pass


class UpdateAutoPart(BaseAutoPartForm):
    pass


class DeleteAutoPart(BaseAutoPartForm):
    pass
