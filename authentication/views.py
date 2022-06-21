from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from allauth.socialaccount.providers.gitlab.views import GitLabOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialConnectView
from dj_rest_auth.registration.views import SocialLoginView
from django.config import settings


class GitHubLogin(SocialLoginView):
    adapter_class = GitHubOAuth2Adapter
    callback_url = settings.CALL_BACK_URL
    client_class = OAuth2Client


class GitLabLogin(SocialLoginView):
    adapter_class = GitLabOAuth2Adapter
    callback_url = settings.CALL_BACK_URL
    client_class = OAuth2Client


class GitHubConnect(SocialConnectView):
    adapter_class = GitHubOAuth2Adapter
    callback_url = settings.CALL_BACK_URL
    client_class = OAuth2Client


class GitLabConnect(SocialConnectView):
    adapter_class = GitLabOAuth2Adapter
    callback_url = settings.CALL_BACK_URL
    client_class = OAuth2Client
