from django.db import models
from pathlib import Path


class Django_Project(models.Model):
    home = Path.home()
    base_path = home / "PycharmProjects"
    project_path=models.FilePathField(path=str(base_path), recursive=False, allow_folders=True, allow_files=False)

class Django_Project2(models.Model):
    home = Path.home()
    base_path = home / "PycharmProjects"
    project_path=models.FilePathField(path=str(base_path), recursive=False, allow_folders=False, allow_files=True)

class Django_Project3(models.Model):
    home = Path.home()
    base_path = home / "PycharmProjects"    
    project_path=models.FilePathField(path=str(base_path), recursive=False, allow_folders=True, allow_files=True)


class Django_Project4(models.Model):
    home = Path.home()
    base_path = home / "PycharmProjects"    
    project_path=models.FilePathField(path=str(base_path), recursive=True, allow_folders=True, allow_files=False)

class Django_Project5(models.Model):
    home = Path.home()
    base_path = home / "PycharmProjects"    
    project_path=models.FilePathField(path=str(base_path), recursive=False, match="fds", allow_folders=True, allow_files=False)
