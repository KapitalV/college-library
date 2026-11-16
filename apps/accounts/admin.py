from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import StaffProfile

class StaffProfileInline(admin.StackedInline):
    model = StaffProfile
    can_delete = False
    verbose_name_plural = 'Staff Profile'

class UserAdmin(BaseUserAdmin):
    inlines = (StaffProfileInline,)
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'get_role')

    def get_role(self, obj):
        if hasattr(obj, 'staff_profile'):
            return obj.staff_profile.get_role_display()
        return '-'
    get_role.short_description = 'Library Role'

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

