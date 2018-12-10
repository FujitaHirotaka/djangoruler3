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

exec(aaa)

class FlexContainerProperty(forms.Form):
      alignitems=forms.ChoiceField(label="align-items", choices=[(0,"stretch"),(1,"flex-start"),(2,"flex-end"),(3,"center"),(4,"baseline"),])
      justifycontent=forms.ChoiceField(label="justify-content", choices=[(0,"flex-start"),(1,"flex-end"),(2,"center"),(3,"space-between"),(4,"space-around"),])
      aligncontent=forms.ChoiceField(label="align-content", choices=[(0,"flex-start"),(1,"flex-end"),(2,"center"),(3,"space-between"),(4,"space-around"),(5,"stretch"),])      
      flexwrap=forms.ChoiceField(label="flex-wrap", choices=[(0,"nowrap"),(1,"wrap"),(2,"wrap-reverse"),])     
      flexdirection=forms.ChoiceField(label="flex-direction", choices=[(0,"row"),(1,"row-reverse"),(2,"column"),(2,"column-reverse"),])       


      