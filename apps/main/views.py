from rest_framework.decorators import api_view
from rest_framework import permissions, generics, status
from rest_framework.reverse import reverse
from rest_framework.response import Response
from apps.main import models, serializers


@api_view(['GET'])
def api_root(request):
    # TODO: Remove this view in the future if we use DefaultRouter.
    """
    This view provides a list of
    all the endpoints available
    on flipify.
    """
    urls = {
        'greet': reverse('greet', request=request),
        'login': reverse('token_obtain_pair', request=request),
        'login-refresh': reverse('token_refresh', request=request),
        'github-login': reverse('github_login', request=request),
        'gitlab-login': reverse('gitlab_login', request=request),
        'github-connect': reverse('github_connect', request=request),
        'gitlab-connect': reverse('gitlab_connect', request=request),
        'platforms': reverse('platform_list', request=request),
        'technologies': reverse('tech_list', request=request),
    }
    return Response(urls)


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
    """
    queryset = models.Platform.objects.all()
    serializer_class = serializers.PlatformSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TechnologyView(generics.ListAPIView):
    """
    Returns a list of technologies or frameworks
    supported by flipify.
    """
    queryset = models.Technology.objects.all()
    serializer_class = serializers.TechnologySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
