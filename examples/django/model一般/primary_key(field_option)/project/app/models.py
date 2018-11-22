from django.db import models
from pathlib import Path

class Player(models.Model):
    name=models.CharField("選手名", max_length=200, primary_key=True)    
    def __str__(self):
         return self.name