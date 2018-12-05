from django import forms
from .models import *
from django.urls import reverse
from django.urls import reverse_lazy


class CssForm(forms.Form):
    value=forms.ChoiceField(label="background-originの値", choices=[(0, "border-box"),(1, "padding-box"),(2, "content-box"), ])
