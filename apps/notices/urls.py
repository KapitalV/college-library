from django.urls import path
from . import views

app_name = 'notices'

urlpatterns = [
    path('', views.notice_list, name='notice_list'),
    path('<slug:slug>/', views.notice_detail, name='notice_detail'),
]

