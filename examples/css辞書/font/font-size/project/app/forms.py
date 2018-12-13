from django import forms
from .models import *
from django.urls import reverse
from django.urls import reverse_lazy
from pathlib import Path



class CssForm(forms.Form):
    value1=forms.ChoiceField(label="font-style", choices=((0,"4px"), (1,"4em"),(2,"4ex"), (3,"70%"),(4,"100%"), (5,"130%"),(6,"xx-small"), (7,"x-small"),(8,"small"), (9,"medium"),(10,"large"), (11,"x-large"),(12,"xx-large"),))