from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)


# Note: Auth urls have been moved to its app.
urlpatterns = [
    path('', views.api_root),
    path('greet/', views.greet, name='greet'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login-refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('platforms/', views.PlatformView.as_view(), name='platform_list'),
    path('technologies/', views.TechnologyView.as_view(), name='tech_list'),
]
