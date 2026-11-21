from django.contrib import admin
from .models import Test


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'duration_minutes', 'passing_score', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title',)
