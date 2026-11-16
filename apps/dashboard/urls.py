from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.dashboard_overview, name='overview'),
    
    # Books
    path('books/', views.dashboard_book_list, name='book_list'),
    path('books/create/', views.dashboard_book_create, name='book_create'),
    path('books/<int:pk>/edit/', views.dashboard_book_edit, name='book_edit'),
    path('books/<int:pk>/delete/', views.dashboard_book_delete, name='book_delete'),
    path('books/<int:book_id>/copies/', views.dashboard_book_copies, name='book_copies'),
    path('copies/<int:pk>/delete/', views.dashboard_copy_delete, name='copy_delete'),
    
    # CSV
    path('books/export-csv/', views.export_books_csv, name='export_books_csv'),
    path('books/import-csv/', views.import_books_csv, name='import_books_csv'),
    
    # Resources
    path('resources/', views.dashboard_resource_list, name='resource_list'),
    path('resources/create/', views.dashboard_resource_create, name='resource_create'),
    path('resources/<int:pk>/edit/', views.dashboard_resource_edit, name='resource_edit'),
    path('resources/<int:pk>/delete/', views.dashboard_resource_delete, name='resource_delete'),
    
    # Notices
    path('notices/', views.dashboard_notice_list, name='notice_list'),
    path('notices/create/', views.dashboard_notice_create, name='notice_create'),
    path('notices/<int:pk>/edit/', views.dashboard_notice_edit, name='notice_edit'),
    path('notices/<int:pk>/delete/', views.dashboard_notice_delete, name='notice_delete'),
    
    # Student Services & Workflow Management
    path('memberships/', views.dashboard_memberships, name='memberships'),
    path('memberships/<int:pk>/update/', views.dashboard_membership_update, name='membership_update'),
    path('recommendations/', views.dashboard_recommendations, name='recommendations'),
    path('recommendations/<int:pk>/update/', views.dashboard_recommendation_update, name='recommendation_update'),
    path('requests/', views.dashboard_requests, name='requests'),
    path('requests/<int:pk>/update/', views.dashboard_request_update, name='request_update'),
    path('feedback/', views.dashboard_feedback, name='feedback'),
    
    # Settings
    path('settings/', views.dashboard_settings, name='settings'),
]

