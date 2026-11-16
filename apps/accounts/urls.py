from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.staff_login_view, name='login'),
    path('logout/', views.staff_logout_view, name='logout'),
    path('profile/', views.staff_profile_view, name='profile'),
]

