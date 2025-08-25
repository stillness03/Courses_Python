from django.urls import path
from . import views

urlpatterns = [
    path('', views.popular_list, name='index'),
    path('courses/', views.course_list, name='course_list'),
    path('courses/<slug:slug>/', views.course_detail, name='course_detail'),
]