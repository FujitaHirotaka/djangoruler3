from django import forms
from .models import *
from django.urls import reverse
from django.urls import reverse_lazy
from pathlib import Path

bathpath=Path.cwd()/"app"/"static"/"app"/"images"

class CssForm(forms.Form):
    source=forms.FilePathField(label="border-image-source", path=bathpath, recursive=False, allow_folders=False, allow_files=True)
    slice=forms.IntegerField(label="border-image-slice")
    width=forms.IntegerField(label="border-image-width")
    outset=forms.IntegerField(label="border-image-outset")
    repeat=forms.ChoiceField(label="border-image-repeat", choices=[(0,"stretch"),(1,"round"),(2,"repeat"),(3,"space"),])    