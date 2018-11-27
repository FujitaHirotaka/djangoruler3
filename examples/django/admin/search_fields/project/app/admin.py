from django.contrib import admin
from .models import *

class BaseballPlayerAdmin(admin.ModelAdmin):
    list_display = ['team', 'name', 'draft', 'birth', 'pub_date']#この順番にadminサイトで表示される。
    list_display_links = ('name','draft')
    list_filter=["birth"]
    search_fields=["name", "team","draft"]


admin.site.register(BaseballPlayer,BaseballPlayerAdmin)

# Register your models here.
