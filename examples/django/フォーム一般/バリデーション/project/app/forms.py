from django import forms
from .models import *
from django.urls import reverse
from django.urls import reverse_lazy
from django import forms
from django.utils import timezone
import re
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator, EmailValidator
from django.core.validators import validate_email

#multiemailfieldというfieldを作りvalidateメソッドでバリデーターを記述
class MultiEmailField(forms.CharField):#forms.Fieldを継承してもよい。
    def to_python(self, value):
        """Normalize data to a list of strings."""
        # Return an empty list if no input was given.
        if not value:
            return []
        return value.split(',')

    def validate(self, value):
        """Check if value consists only of valid emails."""
        # Use the parent's handling of required fields, etc.
        super().validate(value)
        for email in value:
            validate_email(email)


#カラブルの形でバリデーターを記述
def validate_length(value):
    if len(value)>10 or len(value)<3:
        raise ValidationError(
            ('length of %(value)s is not between 3 and 10'), code="error1",
            params={'value': value},
        )

class Form(forms.Form):
    name= forms.CharField(label="ページ名", required=True, help_text="ページ名入力", validators=[validate_length])
    #組み込みバリデーター（MaxValueValidator,MinValueValidator)
    integer=forms.IntegerField(label="数", required=True, help_text="数値入力", validators=[MaxValueValidator(100), MinValueValidator(1)])
    url= forms.URLField(label="URL", required=True, help_text="URL入力")
    #CharFieldとEmailValidatorを使ってEmailField的な使い方
    email= forms.CharField(label="email", required=True, help_text="E-mail入力", validators=[EmailValidator(message="正しいEmailを入力")])
    
    multiemail= MultiEmailField(label="multiemail", required=True, help_text="E-mail入力")
    #clean_(fieldname)メソッドで特定のフィールドのバリデーター
    def clean_name(self):
        data = self.cleaned_data['name']
        if(data.find('<') != -1 or data.find('>') != -1):
            raise forms.ValidationError("名前にタグは使えません")
        return data
    #cleanメソッドで複数のフィールドにまたがるバリデーター
    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        email = cleaned_data.get("email")

        if name and email:
            # Only do something if both fields are valid so far.
            if name not in email:
                raise forms.ValidationError(
                    "email must include name"
                    "OK?"
                )
