from django import forms
from .models import *
from django.urls import reverse
from django.urls import reverse_lazy


class PlayerForm(forms.ModelForm):
    class Meta:
        model=Player
        fields="__all__"
        widgets = {
            'title': forms.CheckboxSelectMultiple(attrs={'class': 'special'}),
            'team': forms.RadioSelect,
            'name': forms.TextInput,
            'gender': forms.RadioSelect,
            'login': forms.RadioSelect,
        
        }
