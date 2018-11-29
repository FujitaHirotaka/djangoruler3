from django import forms
from django.urls import reverse
from django.urls import reverse_lazy
from django import forms
from .models import (
    Player, Title, Team,
    GENDER_CHOICES, TIME_CHOICES,
)
 
 
class PlayerForm(forms.ModelForm):#それぞれのフィールドをオーバーライド
    title = forms.ModelMultipleChoiceField(
        label="タイトル",
        queryset=Title.objects.all(),
        widget=forms.CheckboxSelectMultiple,  # 複数選択チェックボックスへ変更。デフォルトはSelectMultiple
    )
 
    team = forms.ModelChoiceField(
        label="所属チーム",
        queryset=Team.objects.all(),
        widget=forms.RadioSelect,  # ラジオに変更。デフォルトはSelect
        empty_label=None,
    )

    gender = forms.ChoiceField(
        label="性別",
        choices=GENDER_CHOICES,
        widget=forms.RadioSelect,  # ラジオに変更
    )
 
    login = forms.ChoiceField(
        label="ログイン可能時間",
        choices=TIME_CHOICES,
        widget=forms.RadioSelect,  # ラジオに変更
    )

        
 

         
    class Meta:
        model=Player
        fields="__all__"


  
 
