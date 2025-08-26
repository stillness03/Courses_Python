from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('', include('main.urls')),
    path('admin-panel/', include("admin_panel.urls")),
]
