from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.main.urls')),
    path('api/auth/', include('apps.authentication.urls')),
    # To provide the login and logout view in the browsable api.
    # Not essential to the project but included for now.
    path('api-auth/', include('rest_framework.urls')),
]
