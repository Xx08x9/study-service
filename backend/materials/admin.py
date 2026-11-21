from django.contrib import admin
from .models import Material


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'material_type', 'created_at')
    list_filter = ('material_type',)

    search_fields = ('title', 'description')

