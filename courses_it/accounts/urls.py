from django.urls import path
from .views import RegisterView, CustomTokenObtainPairView, LogoutView
from rest_framework_simplejwt.views import TokenRefreshView
from . import views

urlpatterns = [
    # API
    path('api/register/', RegisterView.as_view(), name='api_register'),
    path('api/login/', CustomTokenObtainPairView.as_view(), name='api_login'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='api_token_refresh'),
    path('api/logout/', LogoutView.as_view(), name='api_logout'),

    # Frontend pages
    path("register/", views.register_page, name="register"),
    path("login/", views.login_page, name="login"),
    path("dashboard/", views.dashboard_page, name="dashboard"),
    path("logout/", views.logout_page, name="logout"),
]