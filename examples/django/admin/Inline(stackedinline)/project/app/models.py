from django.db import models
from pathlib import Path


class Team(models.Model):
        name=models.CharField("チーム名", max_length=255)
        def __str__(self):
                return self.name



class BaseballPlayer(models.Model):
        name=models.CharField("名前",max_length=255)
        team=models.ForeignKey(Team, verbose_name="所属チーム", on_delete=models.CASCADE)
        birth=models.DateField("生年月日")    
        def __str__(self):
                return self.name    
        class Meta:
                verbose_name_plural="選手"

    







                   
    

       