from django.contrib import admin
from .models import LibraryStaff, LibraryCommitteeMember, Facility, FAQ

@admin.register(LibraryStaff)
class LibraryStaffAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'role_type', 'email', 'phone', 'display_order', 'is_active')
    list_filter = ('role_type', 'is_active')
    search_fields = ('name', 'designation', 'qualification')

@admin.register(LibraryCommitteeMember)
class LibraryCommitteeMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'department', 'committee_role', 'display_order')
    search_fields = ('name', 'designation', 'department')

@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):
    list_display = ('title', 'capacity', 'timings', 'display_order', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title', 'description', 'features')

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'category', 'display_order', 'is_active')
    list_filter = ('category', 'is_active')
    search_fields = ('question', 'answer')

