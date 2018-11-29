from django import forms
from .models import *
from django.urls import reverse
from django.urls import reverse_lazy
from .models import Img
 
 
class ImgForm(forms.ModelForm):
 
    class Meta:
        model = Img
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={
                'class': "form-control",
            }),
            'file': forms.ClearableFileInput(attrs={
                'class': "form-control-file",
            }),
        }