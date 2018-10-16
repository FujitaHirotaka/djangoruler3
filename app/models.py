from django.db import models

class AppSpecie_type(models.Model):
    type=models.CharField("アプリの必要情報の型", max_length=255)
    def __str__(self):
        return self.type

class AppSpecie(models.Model):
    name=models.CharField("アプリの種類", max_length=255, unique=True)
    type=models.ForeignKey(AppSpecie_type, on_delete=models.CASCADE, blank=True, null=True, verbose_name="アプリの必要情報の型")
    def __str__(self):
        return self.name

class DjangoProject(models.Model):
    project_name=models.CharField("プロジェクト名", max_length=255, unique=True)
    for i in range(1,11):
        exec("app"+str(i)+"=models.CharField('アプリ"+str(i)+"', max_length=255, null=True, blank=True)")
        exec("app" + str(i) + "_URL=models.URLField('URL" + str(i) + "', null=True, blank=True)")
        exec("app"+str(i)+"_specie=models.ForeignKey(AppSpecie, on_delete=models.CASCADE, related_name='アプリ"+str(i)+"', null=True, blank=True)")
    def __str__(self):
        return self.project_name
