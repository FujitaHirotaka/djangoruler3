from django import forms
from .models import *
from django.urls import reverse
from django.urls import reverse_lazy


class CssForm(forms.Form):
    value=forms.ChoiceField(label="background-sizeの値", choices=[(0, "auto"),(1, "contain"),(2, "cover"),(3, "パーセンテージ"),(4, "長さ"), ])
    width=forms.IntegerField(label="長さ", required=False)
    height=forms.IntegerField(label="高さ", required=False)   
 