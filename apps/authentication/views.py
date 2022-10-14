from allauth.socialaccount.providers.github import views as github_views
from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from allauth.socialaccount.providers.gitlab import views as gitlab_views
from allauth.socialaccount.providers.gitlab.views import GitLabOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialConnectView, SocialLoginView
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny


class GitHubLogin(SocialLoginView):
    """Login to Flipify via GitHub.

    This endpoint allows you to complete the login process after which the `code` has been obtained in the frontend
    app using GitHub's Webflow. while the model provides options for `access_token`, `code` and `id_token`. You're to
    provide only the `code` obtained from the frontend in your request.
    """

    adapter_class = GitHubOAuth2Adapter
    callback_url = settings.GITHUB_CALLBACK_URL
    client_class = OAuth2Client


class GitLabLogin(SocialLoginView):
    """Login to Flipify via GitLab."""

    adapter_class = GitLabOAuth2Adapter
    callback_url = settings.GITHUB_CALLBACK_URL
    client_class = OAuth2Client


class GitHubConnect(SocialConnectView):
    """Connect an existing Flipify account to your GitHub Account"""

    permission_classes = (AllowAny,)
    adapter_class = GitHubOAuth2Adapter
    callback_url = settings.GITHUB_CALLBACK_URL
    client_class = OAuth2Client

    def post(self, request, *args, **kwargs):
        """
        Allows users with already existing accounts connect their
        github account.
        """
        return super().post(request, *args, **kwargs)


class GitLabConnect(SocialConnectView):
    """Connect an existing Flipify account to your GitLab Account"""

    permission_classes = (AllowAny,)
    adapter_class = GitLabOAuth2Adapter
    callback_url = settings.GITLAB_CALLBACK_URL
    client_class = OAuth2Client

    def post(self, request, *args, **kwargs):
        """
        Allows users with already existing accounts connect their
        gitlab account.
        """
        return super().post(request, *args, **kwargs)
