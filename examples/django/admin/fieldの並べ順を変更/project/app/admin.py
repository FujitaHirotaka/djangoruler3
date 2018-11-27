from django.contrib import admin
from .models import *

class BaseballPlayerAdmin(admin.ModelAdmin):
    fields = ['team', 'name', 'draft', 'birth', 'pub_date']#この順番にadminサイトで表示される。


admin.site.register(BaseballPlayer,BaseballPlayerAdmin)

# Register your models here.
