from django.db import models

class AppSpecie(models.Model):
    specie=models.CharField("アプリ種", max_length=255, unique=True)

class DjangoProject(models.Model):
    project_name=models.CharField("プロジェクト名", max_length=255, unique=True)
    for i in range(1,11):
        exec("app"+str(i)+"=models.CharField('アプリ"+str(i)+"', max_length=255, null=True, blank=True)")
        exec("app" + str(i) + "_URL=models.URLField('URL" + str(i) + "', null=True, blank=True)")
        #アプリ種との紐づけをのちのちやらなければならない

