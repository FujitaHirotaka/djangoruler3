from django.db import models
from pathlib import Path

def get_next():
    try:
        return Inc.objects.latest('pk').increment_num + 1#pkが重要
    except:
        return 1




class Inc(models.Model):

        increment_num=models.IntegerField(default=get_next )   #default=get_nextとdefault=get_next()の挙動の違いを把握しておく






                   
    

       