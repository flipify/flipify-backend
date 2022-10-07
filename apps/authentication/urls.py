from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import path
from apps.authentication.views import (
    GitHubLogin,
    GitLabLogin,
    GitHubConnect,
    GitLabConnect,
    register,
    profile,
)

urlpatterns = [
    path("github/", GitHubLogin.as_view(), name="github_login"),
    path("gitlab/", GitLabLogin.as_view(), name="gitlab_login"),
    path("github/connect/", GitHubConnect.as_view(), name="github_connect"),
    path("gitlab/connect/", GitLabConnect.as_view(), name="gitlab_connect"),
    path("register/", register, name="register"),
    path("profile/", profile, name="profile"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="authentication/login.html"),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(template_name="authentication/logout.html"),
        name="logout",
    ),
]
