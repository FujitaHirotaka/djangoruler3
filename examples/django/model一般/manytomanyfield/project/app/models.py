from django.db import models
from pathlib import Path

class Player(models.Model):
    name=models.CharField("選手名", max_length=200)    
    def __str__(self):
         return self.name

class Team(models.Model):
    name=models.CharField("チーム名", max_length=200)   
    players=models.ManyToManyField(Player, verbose_name="所属選手") 
    def __str__(self):
         return self.name