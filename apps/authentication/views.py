from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from allauth.socialaccount.providers.gitlab.views import GitLabOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialConnectView
from dj_rest_auth.registration.views import SocialLoginView
from django.conf import settings

from .forms import UserRegisterForm


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


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(
                request, f"Your account has been created! You are now able to log in"
            )
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, "authentication/register.html", {"form": form})


@login_required
def profile(request):
    return render(request, "authentication/profile.html")
