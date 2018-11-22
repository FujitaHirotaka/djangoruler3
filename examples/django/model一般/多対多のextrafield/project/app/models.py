from django.db import models
from pathlib import Path

class Player(models.Model):
    name=models.CharField("選手名", max_length=200)    
    def __str__(self):
         return self.name

class Team(models.Model):
    name=models.CharField("チーム名", max_length=200)   
    players=models.ManyToManyField(Player, through="Membership", verbose_name="所属選手") 
    def __str__(self):
         return self.name

class Membership(models.Model):
    player=models.ForeignKey(Player, verbose_name="選手", on_delete=models.CASCADE)
    team=models.ForeignKey(Team, verbose_name="過去所属したチーム", on_delete=models.CASCADE)
    relationship=models.CharField("関係性", max_length=200)
    def __str__(self):
        return str(self.player.name)+"-"+str(self.team.name)