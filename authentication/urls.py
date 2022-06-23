from django.urls import path
from authentication.views import (
    GitHubLogin,
    GitLabLogin,
    GitHubConnect,
    GitLabConnect
)

urlpatterns = [
    path('github/', GitHubLogin.as_view(), name='github_login'),
    path('gitlab/', GitLabLogin.as_view(), name='gitlab_login'),
    path('github/connect/', GitHubConnect.as_view(), name='github_connect'),
    path('gitlab/connect/', GitLabConnect.as_view(), name='gitlab_connect')
]
