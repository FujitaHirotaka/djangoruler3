from django import forms
from .models import *
from django.urls import reverse
from django.urls import reverse_lazy


class CssForm(forms.Form):
    value=forms.ChoiceField(label="background-originの値", choices=[(0, "repeat"),(1, "repeat-x"),(2, "repeat-y"),(3, "no-repeat"), ])
