from django.contrib import admin

from .models import Guitar


class GuitarConfig(admin.ModelAdmin):
    pass


admin.site.register(Guitar, GuitarConfig)
