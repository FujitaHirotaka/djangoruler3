from django.db import models
from pathlib import Path
import os

def get_upload_to(instance, filename):
    return os.path.join(str(instance.category.name), filename)

class Category(models.Model):
    name=models.CharField("カテゴリー", max_length=255)
    def __str__(self):
        return self.name

class File(models.Model):
    title=models.CharField("ファイル名", max_length=255)
    category=models.ForeignKey(Category, verbose_name="カテゴリー", on_delete=models.CASCADE)
    file=models.FileField(upload_to=get_upload_to)
    def __str__(self):
        return self.title
    def get_filename(self):
        return os.path.basename(self.file.name)