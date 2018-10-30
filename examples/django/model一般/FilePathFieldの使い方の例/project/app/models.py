from django.db import models
from pathlib import Path

class Django_Project(models.Model):
    home = Path.home()
    base_path = home / "PycharmProjects" 
    project_path=models.FilePathField(path=base_path, recursive=False, allow_folders=True, allow_files=False)
