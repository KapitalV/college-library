from .models import SiteSettings, MenuItem
from apps.departments.models import Department
from apps.notices.models import Notice

def library_context(request):
    """
    Global context processor providing site settings, navigation items,
    active departments, and unread/urgent notice counters to all templates.
    """
    try:
        settings_obj = SiteSettings.load()
    except Exception:
        settings_obj = None

    try:
        departments = Department.objects.filter(is_active=True).order_by('display_order', 'name')
    except Exception:
        departments = []

    try:
        menu_items = MenuItem.objects.filter(is_active=True, parent__isnull=True).prefetch_related('children').order_by('order', 'id')
    except Exception:
        menu_items = []

    try:
        pinned_notices = Notice.objects.filter(is_active=True, is_pinned=True).order_by('-publish_date')[:5]
    except Exception:
        pinned_notices = []

    return {
        'site_settings': settings_obj,
        'nav_departments': departments,
        'nav_menu_items': menu_items,
        'pinned_notices': pinned_notices,
    }

