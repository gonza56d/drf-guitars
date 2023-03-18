from django.contrib import admin

from .models import Brand


class BrandConfig(admin.ModelAdmin):
    pass


admin.site.register(Brand, BrandConfig)
