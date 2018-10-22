# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Light

class LightAdmin(admin.ModelAdmin):
    list_display = ('id', 'status')
    list_editabe = ('status',)

    list_filter = ('status',)


admin.site.register(Light, LightAdmin)

# Register your models here.
