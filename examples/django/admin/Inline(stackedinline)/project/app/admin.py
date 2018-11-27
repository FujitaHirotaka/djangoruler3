from django.contrib import admin
from .models import *


class BaseballPlayerInline(admin.StackedInline):
    model = BaseballPlayer
    extra = 10

class TeamAdmin(admin.ModelAdmin):
    fieldsets = [
        ('チーム',               {'fields': ['name']}),
    ]
    inlines = [BaseballPlayerInline]
admin.site.register(Team,TeamAdmin)


# Register your models here.
