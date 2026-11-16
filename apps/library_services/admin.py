from django.contrib import admin
from .models import MembershipApplication, BookRecommendation, ResourceRequest, DownloadableForm

@admin.register(MembershipApplication)
class MembershipApplicationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'roll_number', 'applicant_type', 'department', 'semester', 'status', 'card_number', 'created_at')
    list_filter = ('status', 'applicant_type', 'department', 'semester')
    search_fields = ('full_name', 'roll_number', 'enrollment_number', 'email', 'card_number')

@admin.register(BookRecommendation)
class BookRecommendationAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'recommender_name', 'recommender_role', 'department', 'status', 'created_at')
    list_filter = ('status', 'recommender_role', 'department')
    search_fields = ('title', 'author', 'recommender_name')

@admin.register(ResourceRequest)
class ResourceRequestAdmin(admin.ModelAdmin):
    list_display = ('subject_name', 'request_type', 'requester_name', 'department', 'status', 'created_at')
    list_filter = ('status', 'request_type', 'department')
    search_fields = ('subject_name', 'requester_name', 'details')

@admin.register(DownloadableForm)
class DownloadableFormAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'order', 'is_active')
    list_filter = ('is_active',)

