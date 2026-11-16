"""
URL Configuration for College Library Portal.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.core.urls', namespace='core')),
    path('accounts/', include('apps.accounts.urls', namespace='accounts')),
    path('dashboard/', include('apps.dashboard.urls', namespace='dashboard')),
    path('catalog/', include('apps.catalog.urls', namespace='catalog')),
    path('resources/', include('apps.resources.urls', namespace='resources')),
    path('digital-library/', include(('apps.resources.urls_digital', 'digital_library'), namespace='digital_library')),
    path('departments/', include('apps.departments.urls', namespace='departments')),
    path('notices/', include('apps.notices.urls', namespace='notices')),
    path('services/', include('apps.library_services.urls', namespace='services')),
    path('events/', include('apps.events.urls', namespace='events')),
    path('feedback/', include('apps.feedback.urls', namespace='feedback')),
    path('', include('apps.pages.urls', namespace='pages')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = 'apps.core.views.custom_404_view'
handler500 = 'apps.core.views.custom_500_view'

