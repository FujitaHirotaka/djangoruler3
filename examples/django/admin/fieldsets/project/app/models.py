from django.db import models
from pathlib import Path





class BaseballPlayer(models.Model):
        pub_date=models.DateTimeField("登録日時")
        name=models.CharField("名前",max_length=255)
        team=models.CharField("所属チーム",max_length=255)
        draft=models.CharField("ドラフト情報",max_length=255)
        birth=models.DateField("生年月日")    
        def __str__(self):
                return self.name    
    







                   
    

       