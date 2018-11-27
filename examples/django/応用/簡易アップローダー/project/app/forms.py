from django import forms
from django.urls import reverse
from django.urls import reverse_lazy
from .models import *

class FileForm(forms.ModelForm):
    class Meta:
        model=File
        fields="__all__"

