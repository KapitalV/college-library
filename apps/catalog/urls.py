from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.catalog_search, name='search'),
    path('new-arrivals/', views.new_arrivals, name='new_arrivals'),
    path('donations/', views.donations_list, name='donations'),
    path('<slug:slug>/', views.book_detail, name='book_detail'),
]

