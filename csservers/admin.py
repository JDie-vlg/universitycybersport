from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


# Register your models here.


@admin.register(Server)
class ServerAdmin(admin.ModelAdmin):
    list_display = ('id', 'host', 'port', 'slug')
    list_display_links = ('id', 'host')
    search_fields = ['host', ]
