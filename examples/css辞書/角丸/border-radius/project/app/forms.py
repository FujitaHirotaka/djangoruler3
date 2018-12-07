from django import forms
from .models import *
from django.urls import reverse
from django.urls import reverse_lazy


class CssForm(forms.Form):
    value1=forms.IntegerField(label="左上横")
    value2=forms.IntegerField(label="右上横")
    value3=forms.IntegerField(label="右下横")
    value4=forms.IntegerField(label="左下横")
    value5=forms.IntegerField(label="左上縦")
    value6=forms.IntegerField(label="右上縦")
    value7=forms.IntegerField(label="右下縦")
    value8=forms.IntegerField(label="左下縦")
    unit=forms.ChoiceField(label="単位", choices=[(0,"em"), (1,"px"), (2,"%")])