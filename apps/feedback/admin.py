from django.contrib import admin
from .models import Feedback

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'user_type', 'category', 'rating', 'subject', 'is_reviewed', 'created_at')
    list_filter = ('is_reviewed', 'user_type', 'category', 'rating')
    search_fields = ('name', 'email', 'subject', 'message')

