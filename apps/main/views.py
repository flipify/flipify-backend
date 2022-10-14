from django.shortcuts import redirect
from rest_framework.decorators import api_view
from rest_framework import permissions, generics, status
from django.conf import settings
import requests
from rest_framework.reverse import reverse
from rest_framework.response import Response
from apps.main import models, serializers


@api_view(
    [
        "GET",
    ]
)
def greet(request):
    """
    Greets the user with a message.
    The `name` is passed as a query parameter.
    """
    if request.method != "GET":
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    name = request.query_params.get("name", "World")
    return Response({"message": f"Hello, {name}!"})


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


# Temporarily for development. Redirects users to the documentation.
def handler_404(request, *args, **kwargs):
    return redirect("schema-swagger-ui")
