from django.contrib import admin
from .models import Commentary


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ['id', 'content_object', 'text', 'created_time', 'user', 'root', 'parent']
