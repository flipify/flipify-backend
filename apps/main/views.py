from django.shortcuts import redirect
from rest_framework.decorators import api_view
from rest_framework import permissions, generics, status
from django.conf import settings
import requests
from rest_framework.reverse import reverse
from rest_framework.response import Response
from apps.main import models, serializers


@api_view(['GET'])
def github_repo_access_path(request):
    """
    This endpoint dynamically provides
    our consumer with the url to have users
    grant us acces to their repositories
    """
    return Response({
        "githubRepoAccessUrl": f"https://github.com/login/oauth/authorize?scope=repo&client_id={settings.GITHUB_CLIENT_ID}"
    })


@api_view(['GET'])
def github_callback(request):
    """
    To get access to github repositories,
    we'll need the user in the frontend
    to hit this URL 
    https://github.com/login/oauth/authorize?scope=repo&client_id=[OUR_CLIENT_ID]
    which will redirect the user to gihub to authorize our app,
    on success, github will hit this endpoint
    providing us with a 'code' in the query
    params that we'll use for authorization.
    we use the code in the query params and
    other payloads to obtain the access token
    to access the github API. for now this 
    endpoint will only spit it out it needs
    to be stored. for future use.

    Note: This implementation can only be tested
    if the project is hosted, because of the callback
    url.

    This is not a perfect solution but is a working
    solution and is subject to changes in the future.

    If you have a better idea, don't hesitate to
    make you modifications..ps - I'm not sure this
    views should be in the main app. If you feel the
    same, put them where they belong. That the Open
    Souce Spirit.
    """
    AUTH_URL = 'https://github.com/login/oauth/access_token'
    GITHUB_CODE = request.query_params.get('code')
    payload = {
        "client_id": settings.GITHUB_CLIENT_ID,
        "client_secret": settings.GITHUB_CLIENT_SECRET,
        "code": GITHUB_CODE
    }
    headers = {
        # Can add other headers.
        "content-type": "application/json"
    }
    resp = requests.post(AUTH_URL, payload)
    if resp.status_code != 400:
        return Response(resp.content)
    print(resp.status_code)
    print(resp.content)
    return Response(status=status.HTTP_417_EXPECTATION_FAILED, data={
        'detail': 'An error occured while trying to get the auth token that give\
us read/write access to your repo.'
    })  # Just for testing purposes.


@api_view(['GET', ])
def greet(request):
    """
    Greets the user with a message.
    The `name` is passed as a query parameter.
    """
    if request.method != 'GET':
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    name = request.query_params.get('name', 'World')
    return Response({'message': f'Hello, {name}!'})


class PlatformView(generics.ListAPIView):
    """
    Returns a list of platforms a flipify user
    can switch from or switch to and their current
    status.

    Note: You'll have to manually create `Platform`
    model instance form the django admin to have
    this view not return an empty list.
    """
    queryset = models.Platform.objects.all()
    serializer_class = serializers.PlatformSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TechnologyView(generics.ListAPIView):
    """
    Returns a list of technologies or frameworks
    supported by flipify.

    Note: You'll have to manually create `Technology`
    model instance form the django admin to have
    this view not return an empty list.
    """
    queryset = models.Technology.objects.all()
    serializer_class = serializers.TechnologySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
