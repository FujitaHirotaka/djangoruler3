from django.db import models
from pathlib import Path
import os

class Img(models.Model):
    title = models.CharField("タイトル", max_length=255, blank=True)
    file = models.ImageField("ファイル", upload_to='images/', )
    created_at = models.DateTimeField("作成日", auto_now_add=True)
    updated_at = models.DateTimeField("更新日", auto_now=True)
 
    def __str__(self):
        return self.title
 
    def get_filename(self):
        return os.path.basename(self.file.name)






                   
    

       