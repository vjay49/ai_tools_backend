from django.contrib import admin
from django.utils.html import format_html
from .models import Tool

@admin.register(Tool)
class ToolAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'pricing', 'rating', 'image_preview')
    search_fields = ('name', 'category')
    list_filter = ('category',)
    readonly_fields = ('id', 'image_preview')

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        return ""
    image_preview.short_description = 'Image Preview'
