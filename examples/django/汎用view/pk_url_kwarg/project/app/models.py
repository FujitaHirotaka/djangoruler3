from django.db import models
from pathlib import Path

class Team(models.Model):
        name=models.CharField("チーム名", max_length=255)
        def __str__(self):
                return self.name
class Player(models.Model):
        name=models.CharField("選手名", max_length=255)
        team=models.ManyToManyField(Team, verbose_name="過去所属チーム")
        pub_date=models.DateTimeField("登録日")
        def __str__(self):
                return self.name






                   
    

       