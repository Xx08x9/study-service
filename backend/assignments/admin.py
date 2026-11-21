from django.contrib import admin
from .models import Assignment


@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'deadline', 'is_completed', 'created_at')
    list_filter = ('is_completed',)
    search_fields = ('title', 'description')
