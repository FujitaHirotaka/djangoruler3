from django import forms
from .models import *
from django.urls import reverse
from django.urls import reverse_lazy
from pathlib import Path



class CssForm(forms.Form):
    value1=forms.ChoiceField(label="font-style", choices=((0,"'ＭＳ ゴシック'"), (1,"ＭＳ 明朝"),(2,"sans-serif "), (3,"serif "),(4,"cursive"), (5,"fantasy"),(6,"monospace"), (7,"Impact"),(8,"Charcoal"),))