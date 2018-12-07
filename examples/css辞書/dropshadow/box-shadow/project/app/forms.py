from django import forms
from .models import *
from django.urls import reverse
from django.urls import reverse_lazy
from pathlib import Path

bathpath=Path.cwd()/"app"/"static"/"app"/"images"

class CssForm(forms.Form):
    value1=forms.IntegerField(label="第一パラメーター（水平方向の影のオフセット距離 px）", help_text="正負の値可")
    value2=forms.IntegerField(label="第二パラメーター（垂直方向の影のオフセット距離 px）", help_text="正負の値可")
    value3=forms.IntegerField(label="第三パラメーター（ぼかし距離）px", help_text="正の値のみ可")
    value4=forms.IntegerField(label="第四パラメーター（広がり距離）px", help_text="正の値のみ可")
    inset=forms.BooleanField(label="第五パラメーター（inset)", required=False)    