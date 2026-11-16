from django.urls import path
from . import views

urlpatterns = [
    path('', views.digital_library_home, name='home'),
    path('portals/', views.digital_portals, name='portals'),
]

