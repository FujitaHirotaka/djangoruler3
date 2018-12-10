from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotAllowed
import os
from pathlib import Path
import re
from ajax.views import z
from django.views import View
from django.urls import reverse
from django.views import generic
from .forms import *



d = z()
d["mode"] = "index"

def index(request):
    print(list1)  
    print(list2)      
    if request.method=="POST":

          print(request.POST)
          fc=FlexContainerProperty(request.POST)
          dict1={"width":request.POST.getlist("width")[0], "height":request.POST.getlist("height")[0]}
          f1=FlexItem1(dict1)
          dict2={"width":request.POST.getlist("width")[1], "height":request.POST.getlist("height")[1]}          
          f2=FlexItem2(dict2)
          dict3={"width":request.POST.getlist("width")[2], "height":request.POST.getlist("height")[2]}
          f3=FlexItem3(dict3)
          dict4={"width":request.POST.getlist("width")[3], "height":request.POST.getlist("height")[3]}          
          f4=FlexItem4(dict4)
          dict5={"width":request.POST.getlist("width")[4], "height":request.POST.getlist("height")[4]}          
          f5=FlexItem5(dict5)
          dict6={"width":request.POST.getlist("width")[5], "height":request.POST.getlist("height")[5]}          
          f6=FlexItem6(dict6)
          dict7={"width":request.POST.getlist("width")[6], "height":request.POST.getlist("height")[6]}          
          f7=FlexItem7(dict7)
          dict8={"width":request.POST.getlist("width")[7], "height":request.POST.getlist("height")[7]}          
          f8=FlexItem8(dict8)
          dict9={"width":request.POST.getlist("width")[8], "height":request.POST.getlist("height")[8]}          
          f9=FlexItem9(dict9)
          dict10={"width":request.POST.getlist("width")[9], "height":request.POST.getlist("height")[9]}          
          f10=FlexItem10(dict10)
          
          choice_list=f1.fields['width'].choices       
          alignitems_list=fc.fields["alignitems"].choices   
          justifycontent_list=fc.fields["justifycontent"].choices 
          aligncontent_list=fc.fields["aligncontent"].choices           
          flexwrap_list=fc.fields["flexwrap"].choices
          flexdirection_list=fc.fields["flexdirection"].choices            
          if fc.is_valid() and f1.is_valid() and f2.is_valid and f3.is_valid and f4.is_valid and f5.is_valid and f6.is_valid and f7.is_valid and f8.is_valid and f9.is_valid and f10.is_valid:
                 d["form1"]=f1
                 d["form2"]=f2
                 d["form3"]=f3
                 d["form4"]=f4
                 d["form5"]=f5
                 d["form6"]=f6
                 d["form7"]=f7
                 d["form8"]=f8
                 d["form9"]=f9
                 d["form10"]=f10
                 d["formfc"]=fc                                                  
                 with open("app/static/app/base_origin.css", "r") as ff:
                       data = ff.read()
                       if dict1["width"]=="0":
                            data=data.replace("width1", "")
                       else:      
                            data=data.replace("width1", "width:"+choice_list[int(dict1["width"])][1]+"px;")
                       if dict1["height"]=="0":
                            data=data.replace("height1", "")   
                       else:                                
                            data=data.replace("height1", "height:"+choice_list[int(dict1["height"])][1]+"px;")

                       if dict2["width"]=="0":
                            data=data.replace("width2", "")
                       else:      
                            data=data.replace("width2", "width:"+choice_list[int(dict2["width"])][1]+"px;")
                       if dict2["height"]=="0":
                            data=data.replace("height2", "")   
                       else:                                
                            data=data.replace("height2", "height:"+choice_list[int(dict2["height"])][1]+"px;")              
                       if dict3["width"]=="0":
                            data=data.replace("width3", "")
                       else:      
                            data=data.replace("width3", "width:"+choice_list[int(dict3["width"])][1]+"px;")
                       if dict3["height"]=="0":
                            data=data.replace("height3", "")   
                       else:                                
                            data=data.replace("height3", "height:"+choice_list[int(dict3["height"])][1]+"px;")     

                       if dict4["width"]=="0":
                            data=data.replace("width4", "")
                       else:      
                            data=data.replace("width4", "width:"+choice_list[int(dict4["width"])][1]+"px;")
                       if dict4["height"]=="0":
                            data=data.replace("height4", "")   
                       else:                                
                            data=data.replace("height4", "height:"+choice_list[int(dict4["height"])][1]+"px;")   


                       if dict5["width"]=="0":
                            data=data.replace("width5", "")
                       else:      
                            data=data.replace("width5", "width:"+choice_list[int(dict5["width"])][1]+"px;")
                       if dict5["height"]=="0":
                            data=data.replace("height5", "")   
                       else:                                
                            data=data.replace("height5", "height:"+choice_list[int(dict5["height"])][1]+"px;") 



                       if dict6["width"]=="0":
                            data=data.replace("width6", "")
                       else:      
                            data=data.replace("width6", "width:"+choice_list[int(dict6["width"])][1]+"px;")
                       if dict6["height"]=="0":
                            data=data.replace("height6", "")   
                       else:                                
                            data=data.replace("height6", "height:"+choice_list[int(dict6["height"])][1]+"px;") 



                       if dict7["width"]=="0":
                            data=data.replace("width7", "")
                       else:      
                            data=data.replace("width7", "width:"+choice_list[int(dict7["width"])][1]+"px;")
                       if dict7["height"]=="0":
                            data=data.replace("height7", "")   
                       else:                                
                            data=data.replace("height7", "height:"+choice_list[int(dict7["height"])][1]+"px;")      
                       

                       if dict8["width"]=="0":
                            data=data.replace("width8", "")
                       else:      
                            data=data.replace("width8", "width:"+choice_list[int(dict8["width"])][1]+"px;")
                       if dict8["height"]=="0":
                            data=data.replace("height8", "")   
                       else:                                
                            data=data.replace("height8", "height:"+choice_list[int(dict8["height"])][1]+"px;") 


                       if dict9["width"]=="0":
                            data=data.replace("width9", "")
                       else:      
                            data=data.replace("width9", "width:"+choice_list[int(dict9["width"])][1]+"px;")
                       if dict9["height"]=="0":
                            data=data.replace("height9", "")   
                       else:                                
                            data=data.replace("height9", "height:"+choice_list[int(dict9["height"])][1]+"px;") 


                       if dict10["width"]=="0":
                            data=data.replace("widtha", "")
                       else:      
                            data=data.replace("widtha", "width:"+choice_list[int(dict10["width"])][1]+"px;")
                       if dict10["height"]=="0":
                            data=data.replace("heighta", "")   
                       else:                                
                            data=data.replace("heighta", "height:"+choice_list[int(dict10["height"])][1]+"px;") 
                       
                       data=data.replace("**__align-items__**", alignitems_list[int(fc.cleaned_data["alignitems"])][1])
                       data=data.replace("**__justify-content__**", justifycontent_list[int(fc.cleaned_data["justifycontent"])][1])
                       data=data.replace("**__align-content__**", aligncontent_list[int(fc.cleaned_data["aligncontent"])][1])                       
                       data=data.replace("**__flex-wrap__**", flexwrap_list[int(fc.cleaned_data["flexwrap"])][1])
                       data=data.replace("**__flex-direction__**", flexdirection_list[int(fc.cleaned_data["flexdirection"])][1])                       
                       print(int(fc.cleaned_data["alignitems"]))
                 with open("app/static/app/base.css", "w") as ff:
                       ff.write(data)
                 return render(request, "app/index.html", d)
    else:
          f1=FlexItem1()
          f2=FlexItem2()
          f3=FlexItem3()
          f4=FlexItem4()
          f5=FlexItem5()
          f6=FlexItem6()
          f7=FlexItem7()
          f8=FlexItem8()
          f9=FlexItem9()
          f10=FlexItem10()
          fc=FlexContainerProperty()
          d["form1"]=f1
          d["form2"]=f2
          d["form3"]=f3
          d["form4"]=f4
          d["form5"]=f5
          d["form6"]=f6
          d["form7"]=f7
          d["form8"]=f8
          d["form9"]=f9
          d["form10"]=f10
          d["formfc"]=fc
          
          

    return render(request, "app/index.html", d)      


    