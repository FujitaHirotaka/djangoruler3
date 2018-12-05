from django import forms
from .models import *
from django.urls import reverse
from django.urls import reverse_lazy


class CssForm(forms.Form):
    name = forms.CharField(widget=forms.HiddenInput, initial="general")
    value=forms.ChoiceField(label="background-positionの値", choices=[(0, "left"),(1, "center"),(2, "right"), (3, "top"),(4, "bottom"),])


class CssForm_length(forms.Form):
    name = forms.CharField(widget=forms.HiddenInput, initial="length")
    width=forms.IntegerField(label="幅(px)")
    height=forms.IntegerField(label="高さ(px)")


class CssForm_percentage(forms.Form):
    name = forms.CharField(widget=forms.HiddenInput, initial="percentage")    
    width=forms.IntegerField(label="幅(%)")
    height=forms.IntegerField(label="高さ(%)")
