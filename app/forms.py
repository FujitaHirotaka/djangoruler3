from django import forms
from .models import *

class DjangoForm(forms.ModelForm):
    class Meta:
        model=DjangoProject
        fields="__all__"

