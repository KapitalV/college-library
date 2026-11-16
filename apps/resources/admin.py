from django.contrib import admin
from .models import DigitalResource

@admin.register(DigitalResource)
class DigitalResourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'department', 'semester', 'academic_year', 'access_type', 'download_count', 'is_published')
    list_filter = ('category', 'department', 'semester', 'access_type', 'is_published', 'is_featured')
    search_fields = ('title', 'description', 'author_or_faculty', 'academic_year')
    prepopulated_fields = {'slug': ('title',)}

