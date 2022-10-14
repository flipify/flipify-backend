from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.authentication.views import (
    GitHubConnect,
    GitHubLogin,
    GitLabConnect,
    GitLabLogin,
)

from dj_rest_auth.views import LogoutView

urlpatterns = [
    path("logout/", LogoutView.as_view(), name="logout"),
    path("github/", GitHubLogin.as_view(), name="github_login"),
    path("gitlab/", GitLabLogin.as_view(), name="gitlab_login"),
    path("github/connect/", GitHubConnect.as_view(), name="github_connect"),
    path("gitlab/connect/", GitLabConnect.as_view(), name="gitlab_connect"),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("login-refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
