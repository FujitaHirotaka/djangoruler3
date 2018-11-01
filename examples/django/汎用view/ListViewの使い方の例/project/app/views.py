from django.shortcuts import render
import os
from pathlib import Path
import re
from django.views.generic import TemplateView



class index(TemplateView):
    template_name="app/index.html"

    #この部分で変数をテンプレートに渡している。ここではfile_path_listとmax_hierarchy_numberを渡した。
    def get_context_data(self, **kwargs):
        #***************************************
        file_path_list=make_file_path_list()[0]     
        hierarchy_list=make_file_path_list()[1]
        max_hierarchy_number=max(hierarchy_list)
        #*****************************************
        context = super().get_context_data(**kwargs) # はじめに継承元のメソッドを呼び出す
        context["file_path_list"] = file_path_list
        context["max_hierarchy_number"] =max_hierarchy_number
        return context






def make_file_path_list():
        base_path=Path.cwd()
        file_path_list=[]
        hierarchy_list=[]
        for i in base_path.glob("**/*"):
                 if not ("migrations" in str(i)) and not ("rightside.html" in str(i)) and not ("footer.html" in str(i)) and not ("footer_origin.html" in str(i)) and not ("views2.py" in str(i)) and not (".vscode" in str(i)) and not ("db.sqlite" in str(i)) and not ("manage.py" in str(i)) and not ("__pycache__" in str(i)): 
                          mojiretu=str(i).replace(str(base_path)+"\\","")
                          find_list=re.findall("\\\\", mojiretu) #ここ重要
                          for ii in range(len(find_list)):
                                 mojiretu=mojiretu.replace("\\", "/")
                          file_path_list.append(mojiretu)
                          hierarchy_list.append(len(find_list))
        return file_path_list, hierarchy_list

