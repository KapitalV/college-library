from django.urls import path
from . import views

app_name = 'resources'

urlpatterns = [
    path('', views.resource_list, name='resource_list'),
    path('question-papers/', views.question_papers, name='question_papers'),
    path('syllabus/', views.syllabus_list, name='syllabus'),
    path('lecture-notes/', views.lecture_notes, name='lecture_notes'),
    path('download/<slug:slug>/', views.download_resource, name='download'),
    path('<slug:slug>/', views.resource_detail, name='resource_detail'),
]

