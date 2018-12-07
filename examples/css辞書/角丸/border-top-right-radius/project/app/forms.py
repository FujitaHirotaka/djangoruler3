from django import forms
from .models import *
from django.urls import reverse
from django.urls import reverse_lazy


class CssForm(forms.Form):
    value1=forms.IntegerField(label="右上横")
    value5=forms.IntegerField(label="右上縦")
    unit=forms.ChoiceField(label="単位", choices=[(0,"em"), (1,"px"), (2,"%")])