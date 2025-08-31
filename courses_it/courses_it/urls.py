from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('accounts.urls', 'accounts'), namespace='accounts')),
    path('', include('main.urls')),
    path('api/', include('courses.urls')),
    path('admin-panel/', include("admin_panel.urls")),
]
