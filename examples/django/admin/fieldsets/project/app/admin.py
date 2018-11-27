from django.contrib import admin
from .models import *


class BaseballPlayerAdmin(admin.ModelAdmin):
    fieldsets = [
        ('チーム',               {'fields': ['team']}),
        ('名前', {'fields': ['name']}),
        ('入団時の情報', {'fields': ['draft']}),
        ('日付情報', {'fields': ['birth',"pub_date"]}),
    ]

admin.site.register(BaseballPlayer,BaseballPlayerAdmin)

# Register your models here.
