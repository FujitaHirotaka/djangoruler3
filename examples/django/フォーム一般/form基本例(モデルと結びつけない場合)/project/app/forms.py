from django import forms
from .models import *
from django.urls import reverse
from django.urls import reverse_lazy
from django import forms
from django.utils import timezone

CAKE_CHOICES = (
    (1, 'いちごケーキ'),
    (2, 'チョコケーキ'),
    (3, 'チーズケーキ')
)




class Form(forms.Form):
    title = forms.CharField(label="CharField", help_text="名前を入れてください", initial="初期値", max_length=20, min_length=2)
    title2 = forms.SlugField(label="SlugField", help_text="名前を入れてください", initial="abc-def_ghi", max_length=20, min_length=2)
    email=forms.EmailField(label="EmailField", help_text="Eメールアドレスを入れてください")
    url=forms.URLField(label="URLField", help_text="URLを入れてください")
    checkbox=forms.BooleanField(label="BooleanField", help_text="チェックを入れてください")
    checkbox2=forms.NullBooleanField(label="NullBooleanField", help_text="選んでください")
    choice=forms.ChoiceField(label="ChoiceField", help_text="選んでください", choices=CAKE_CHOICES, initial=(2,"チョコケーキ"))
    typechoice=forms.TypedChoiceField(label="TypedChoiceField", help_text="選んでください", choices=CAKE_CHOICES, initial=(2,"チョコケーキ"))
    day=forms.DateField(label="DateField", help_text="", initial=timezone.now)
    daytime=forms.DateTimeField(label="DateTimeField", help_text="日時を入れてください", initial=timezone.now)
    time=forms.TimeField(label="TimeField", help_text="時間を入れてください", initial=timezone.now)    
    

