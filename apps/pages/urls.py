from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('about/', views.about_library, name='about'),
    path('about/vision-mission/', views.vision_mission, name='vision_mission'),
    path('rules/', views.rules_regulations, name='rules'),
    path('staff/', views.library_staff_list, name='staff'),
    path('facilities/', views.facilities_list, name='facilities'),
    path('faq/', views.faq_list, name='faq'),
]

