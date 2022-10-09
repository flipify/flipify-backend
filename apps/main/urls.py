from django.urls import path
from . import views


# Note: Auth urls have been moved to its app.
urlpatterns = [
    path("greet/", views.greet, name="greet"),
    path("platforms/", views.PlatformView.as_view(), name="platform_list"),
    path("technologies/", views.TechnologyView.as_view(), name="tech_list"),
    path("lol/", views.handler_404),
]
