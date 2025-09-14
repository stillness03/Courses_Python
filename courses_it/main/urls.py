from django.urls import path
from . import views

urlpatterns = [
    path('', views.popular_list, name='index'),
    path('home/', views.popular_list, name='home'),
    path('about_us/', views.about_us, name='about_us'),
    path('cost/', views.cost_page, name='cost'),
    path("courses/<slug:slug>/", views.CourseDetail.as_view(), name="course_detail"),
]