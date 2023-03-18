from django.contrib import admin

from .models import Brand, Line


class BrandConfig(admin.ModelAdmin):
    pass


class LineConfig(admin.ModelAdmin):
    pass


admin.site.register(Brand, BrandConfig)
admin.site.register(Line, LineConfig)
