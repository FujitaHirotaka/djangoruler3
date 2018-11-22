from django.db import models
from pathlib import Path
import datetime
from django.utils import timezone

class Teams(models.Model):
     name=models.CharField("チーム名", max_length=10)
     pub_date=models.DateTimeField(verbose_name="作成日")
     def __str__(self):
         return self.name
     def was_published_recently(self):
         return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Players(models.Model):
     name=models.CharField(verbose_name="選手名", max_length=20)
     team=models.ForeignKey(Teams, verbose_name="チーム名", on_delete=models.CASCADE)
     votes=models.IntegerField("票数", default=0)
     def __str__(self):
         return self.name
         

