from django import forms
from .models import *
from django.urls import reverse
from django.urls import reverse_lazy
from pathlib import Path



class CssForm(forms.Form):
    value1=forms.ChoiceField(label="font-style", choices=((0,"100"), (1,"200"),(2,"300"), (3,"400"),(4,"500"), (5,"600"),(6,"700"), (7,"800"),(8,"900"), (9,"normal"),(10,"bold"), (11,"lighter"),(12,"bolder"),))