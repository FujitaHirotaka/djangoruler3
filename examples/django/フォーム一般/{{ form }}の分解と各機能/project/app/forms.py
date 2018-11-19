from django import forms
from .models import *
from django.urls import reverse
from django.urls import reverse_lazy
from django import forms
from django.utils import timezone
import re



class Form(forms.Form):
    name= forms.CharField(label="ページ名", required=True, help_text="ページ名入力")
    url= forms.URLField(label="URL", required=True, help_text="URL入力")
  
    def clean_name(self):
        data = self.cleaned_data['name']
        if(data.find('<') != -1 or data.find('>') != -1):
            raise forms.ValidationError("名前にタグは使えません")
        return data
