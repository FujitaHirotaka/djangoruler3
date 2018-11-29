from django.db import models
from pathlib import Path
from datetime import time
from django.contrib.auth.models import User

GENDER_CHOICES=(
        ("女性","女性"),
        ("男性","男性")
)

TIME_CHOICES=((time(hour, 00,00), "{}時".format(hour)) for hour in range(9,16))

class Title(models.Model):
        name=models.CharField(max_length=255)
        def __str__(self):
                return self.name

class Team(models.Model):
        name=models.CharField(max_length=255)
        def __str__(self):
                return self.name

class Player(models.Model):
    name = models.CharField( "名前", max_length=255)
    title = models.ManyToManyField(Title, verbose_name="過去タイトル")
    team = models.ForeignKey(Team, verbose_name="所属チーム", on_delete=models.CASCADE)
    gender = models.CharField(verbose_name="性別", max_length=2, blank=True, choices=GENDER_CHOICES)
    login = models.TimeField("ログイン可能時間", choices=TIME_CHOICES)
 
    def __str__(self):
        return self.name






                   
    

       