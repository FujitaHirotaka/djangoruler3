from django import forms
from .models import *
from django.urls import reverse
from django.urls import reverse_lazy


class CssForm(forms.Form):
    value=forms.ChoiceField(label="background-repeatの値", choices=[(0, "fixed"),(1, "scroll"),])
