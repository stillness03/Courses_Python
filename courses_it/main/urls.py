from django.urls import path
from . import views
from courses.views import CourseDetail

urlpatterns = [
    path('', views.popular_list, name='index'),
    path('home/', views.popular_list, name='home'),
    path('courses/', views.course_list, name='course_list'),
    path('about_us/', views.about_us, name='about_us'),
    path('cost/', views.cost_page, name='cost'),
    path('courses/<int:course_id>/', CourseDetail.as_view(), name='course_detail'),
]