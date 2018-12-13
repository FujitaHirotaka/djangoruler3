from django import forms
from .models import *
from django.urls import reverse
from django.urls import reverse_lazy
from pathlib import Path



class CssForm(forms.Form):
    value1=forms.ChoiceField(label="font-style", choices=((0,"ultra-condensed"), (1,"extra-condensed"),(2,"condensed"), (3,"semi-condensed"),(4,"normal"), (5,"semi-expanded"),(6,"expanded"), (7,"extra-expanded"),(8,"ultra-expanded"),(9,"wider"),(10,"narrower"),(11,"inherit"),))