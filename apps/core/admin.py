from django.contrib import admin
from django.utils.html import format_html
from .models import SiteSettings, MenuItem, HeroSlide

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ('short_name', 'college_name', 'contact_phone', 'library_email', 'updated_at')
    
    def has_add_permission(self, request):
        # Enforce singleton
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'parent', 'order', 'is_active', 'staff_only')
    list_filter = ('is_active', 'staff_only', 'parent')
    search_fields = ('title', 'url')
    ordering = ('order', 'id')


@admin.register(HeroSlide)
class HeroSlideAdmin(admin.ModelAdmin):
    list_display = ('image_preview', 'title', 'badge_text', 'order', 'is_active', 'link_url', 'created_at')
    list_editable = ('order', 'is_active')
    list_filter = ('is_active', 'badge_text', 'created_at')
    search_fields = ('title', 'subtitle', 'badge_text')
    ordering = ('order', 'id')
    readonly_fields = ('image_preview_large', 'created_at', 'updated_at')
    fieldsets = (
        ("Slide Content", {
            "fields": ("title", "subtitle", "badge_text", "image", "image_preview_large")
        }),
        ("Link & Action (Optional)", {
            "fields": ("link_url", "link_text")
        }),
        ("Display Settings", {
            "fields": ("order", "is_active", "created_at", "updated_at")
        }),
    )

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="width: 80px; height: 45px; object-fit: cover; border-radius: 4px; border: 1px solid #ddd;" />',
                obj.image.url
            )
        return "-"
    image_preview.short_description = "Thumbnail"

    def image_preview_large(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-width: 400px; height: auto; border-radius: 6px; border: 1px solid #ccc;" />',
                obj.image.url
            )
        return "No image uploaded yet"
    image_preview_large.short_description = "Image Preview"


