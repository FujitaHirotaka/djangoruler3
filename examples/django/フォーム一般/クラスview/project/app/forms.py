from django import forms
from .models import *
from django.urls import reverse
from django.urls import reverse_lazy
from django import forms
from django.utils import timezone



class Form(forms.Form):
    number1 = forms.IntegerField(label="number①", help_text="数字限定")
    number2= forms.IntegerField(label="number②", help_text="数字限定")
  
class Form2(forms.Form):
    number1 = forms.IntegerField(label="number①", help_text="数字限定")
    number2= forms.IntegerField(label="number②", help_text="数字限定")    
    number3= forms.IntegerField(label="答え", required=False)    
