import json

from django.contrib import admin

# Register your models here.
from .models import Rock


# class Detailline(admin.StackedInline):
#     model = RockDetail
# 
# 
# class RockAdmin(admin.ModelAdmin):
#     inlines = [Detailline, ]


admin.site.register(Rock)
# admin.site.register(RockDetail)
