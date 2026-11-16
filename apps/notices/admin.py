from django.contrib import admin
from .models import Notice

@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'priority', 'publish_date', 'expiry_date', 'is_pinned', 'is_active')
    list_filter = ('category', 'priority', 'is_pinned', 'is_active', 'publish_date')
    search_fields = ('title', 'short_summary', 'content')
    prepopulated_fields = {'slug': ('title',)}

