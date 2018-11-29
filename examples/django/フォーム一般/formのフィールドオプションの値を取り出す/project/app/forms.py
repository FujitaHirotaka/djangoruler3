from django import forms
from .models import *
from django.urls import reverse
from django.urls import reverse_lazy


class PlayerForm(forms.ModelForm):
    class Meta:
        model=Player
        fields="__all__"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"
