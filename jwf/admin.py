from django.contrib import admin
from . import models


class EventAdmin(admin.ModelAdmin):
    list_display = [
        'date',
        'name',
    ]




admin.site.register(models.Event, EventAdmin)
