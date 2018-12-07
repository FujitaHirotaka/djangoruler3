from django import forms
from .models import *
from django.urls import reverse
from django.urls import reverse_lazy
from pathlib import Path

list1=[(0,"----"), (1,'50'), (2,'100'),(3,'200'),(4,'400'),]
list2=list(range(1,11))

dict={"width":"幅(px)", "height":"高さ(px)"}
aaa=""
for i in list2:
    aaa+="class FlexItem"+str(i)+"(forms.Form):\n"
    for ii in dict.keys():
        aaa+="  "+ii+"=forms.ChoiceField(label='"+dict[ii]+"', choices=list1, required=False)\n"


print(aaa)


exec(aaa)
