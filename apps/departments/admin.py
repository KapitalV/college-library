from django.contrib import admin
from .models import Department, Subject

class SubjectInline(admin.TabularInline):
    model = Subject
    extra = 1

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'head_of_department', 'intake_capacity', 'display_order', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name', 'code', 'head_of_department')
    prepopulated_fields = {'slug': ('code',)}
    inlines = [SubjectInline]

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'department', 'semester', 'is_active')
    list_filter = ('department', 'semester', 'is_active')
    search_fields = ('name', 'code')

