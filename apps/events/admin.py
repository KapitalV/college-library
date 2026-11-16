from django.contrib import admin
from .models import LibraryEvent, GalleryImage

class GalleryImageInline(admin.TabularInline):
    model = GalleryImage
    extra = 2

@admin.register(LibraryEvent)
class LibraryEventAdmin(admin.ModelAdmin):
    list_display = ('title', 'event_type', 'venue', 'start_date', 'end_date', 'is_featured', 'is_active')
    list_filter = ('event_type', 'is_featured', 'is_active', 'start_date')
    search_fields = ('title', 'summary', 'description', 'venue')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [GalleryImageInline]

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'event', 'is_featured_home', 'order', 'created_at')
    list_filter = ('is_featured_home', 'event')
    search_fields = ('title', 'caption')

