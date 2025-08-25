from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_dashboard, name='admin_dashboard'),
    path('courses/', views.admin_courses, name='admin_courses'),
    path('lessons/', views.admin_lessons, name='admin_lessons'),
    path('quizzes/', views.admin_quizzes, name='admin_quizzes'),
    path('payments/', views.admin_payments, name='admin_payments'),
    path('users/', views.admin_users, name='admin_users'),
]