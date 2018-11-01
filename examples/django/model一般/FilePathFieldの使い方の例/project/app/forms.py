from django import forms
from .models import *
from django.urls import reverse
from django.urls import reverse_lazy

class Form(forms.ModelForm):
    class Meta:
        model=Django_Project
        fields='__all__'

class Form2(forms.ModelForm):
    class Meta:
        model=Django_Project2
        fields='__all__'

class Form3(forms.ModelForm):
    class Meta:
        model=Django_Project3
        fields='__all__'

class Form4(forms.ModelForm):
    class Meta:
        model=Django_Project4
        fields='__all__'

class Form5(forms.ModelForm):
    class Meta:
        model=Django_Project5
        fields='__all__'


