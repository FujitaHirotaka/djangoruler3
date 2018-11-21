from django import forms
from .models import *
from django.urls import reverse
from django.urls import reverse_lazy
from django import forms
from django.utils import timezone
from django.core.validators import MinLengthValidator



class Form(forms.Form):
    char1 = forms.CharField(label="文字列", help_text="文字列入力", max_length=100, validators=[MinLengthValidator(10)])
    check= forms.BooleanField(label="チェック", help_text="チェック")
    type = forms.CharField(label="", initial="hidden", required=False, widget=forms.HiddenInput(attrs={"value":"tekitou"}))
  
