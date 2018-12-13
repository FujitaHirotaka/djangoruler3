from django import forms
from .models import *
from django.urls import reverse
from django.urls import reverse_lazy
from pathlib import Path



class CssForm(forms.Form):
    value1=forms.ChoiceField(label="font-style", choices=((0,"normal"), (1,"italic"),(2,"oblique"),))