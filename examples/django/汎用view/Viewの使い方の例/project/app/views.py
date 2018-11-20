from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed
import os
from pathlib import Path
import re
from ajax.views import z
from django.views import View


#この部分は本編とは関係なし
########################
d=z()    
########################




def index(request):
#この部分は本編とは関係なし
########################    
    d["mode"]="index"
########################    
    
    return render(request, 'app/index.html', d)


def index2(request):
#この部分は本編とは関係なし
########################        
    d["mode"]="index2"    
########################       
    if request.method=="GET":
        return render(request, "app/index.html",d)
    else:
       return HttpResponseNotAllowed("GET以外のリクエストメソッドでアクセスしたのでアクセスは認められない") 
    return render(request, 'app/index.html', d)


class Index3(View):
#この部分は本編とは関係なし    
########################        
    d["mode"]="index3"    
########################     
    template_nam="app/index.html"
    def get(self, request, *args, **kwargs):
        return render(request, self.template_nam, d)

index3=Index3.as_view()


class Index4(View):
    
    def get(self, request, *args, **kwargs):
        kwargs.update(d)
        kwargs["mode"]="index4"
        return render(request, "app/index.html", kwargs)

def index4(request, *args, **kwargs):
    view_obj = Index4()
    view_obj.request = request
    view_obj.args = args
    view_obj.kwargs = kwargs
    return view_obj.dispatch(request, *args, **kwargs)







