from django.db import models
from pathlib import Path

team_list=(
    ("G","巨人"),
    ("C","広島"),
    ("S","ヤクルト"),
    ("De","横浜"),
    ("D","中日"),
    ("T","阪神"),                    
)
class Player(models.Model):
    name=models.CharField("選手名", max_length=200, default="菊池涼介")
    team=models.CharField("所属チーム", choices=team_list, max_length=2)
    
