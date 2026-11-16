from django.urls import path
from . import views

app_name = 'services'

urlpatterns = [
    path('', views.service_list, name='service_list'),
    path('membership/', views.membership_apply, name='membership'),
    path('book-recommendation/', views.book_recommend, name='book_recommend'),
    path('resource-request/', views.resource_request, name='resource_request'),
    path('no-dues/', views.no_dues_info, name='no_dues'),
    path('ndli-club/', views.ndli_club_info, name='ndli_club'),
    path('forms/', views.downloadable_forms_list, name='forms'),
]

