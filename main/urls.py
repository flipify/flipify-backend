from django.urls import path
from authentication.views import (
        GitHubLogin,
        GitLabLogin, 
        GitHubConnect,
        GitLabConnect
    )

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)



urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login-refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/github/', GitHubLogin.as_view(), name='github_login'),
    path('auth/gitlab/', GitLabLogin.as_view(), name='gitlab_login'),
    path('auth/github/connect/', GitHubConnect.as_view(), name='github_connect'),
    path('auth/gitlab/connect/', GitLabConnect.as_view(), name='gitlab_connect')
]