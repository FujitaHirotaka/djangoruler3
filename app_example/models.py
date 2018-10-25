from django.db import models
from pathlib import Path
import os

pathlist = ["C://users/sakodaken/pycharmprojects", "C://users/fujita/pycharmprojects"]
for i in pathlist:
    if Path(i).exists():
        directory_of_projectexamples = Path(i) / "djangoruler3" / "project"


class Django_Project(models.Model):
    example_path = models.FilePathField(
        path=str(directory_of_projectexamples),
        recursive=False,
        allow_folders=True,
        allow_files=False,
    )


class LargeCategory(models.Model):
    largecategoryname = models.CharField("大カテゴリー名", max_length=200)

    def __str__(self):
        return self.largecategoryname


class MiddleCategory(models.Model):
    largecategory = models.ForeignKey(
        LargeCategory, on_delete=models.CASCADE, verbose_name="大カテゴリー"
    )
    middlecategoryname = models.CharField("中カテゴリー名", max_length=200)

    def __str__(self):
        return self.middlecategoryname


class SmallCategory(models.Model):
    middlecategory = models.ForeignKey(
        MiddleCategory, on_delete=models.CASCADE, verbose_name="中カテゴリー"
    )
    smallcategoryname = models.CharField("中カテゴリー名", max_length=200)

    def __str__(self):
        return self.middlecategoryname

