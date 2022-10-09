from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

handler404 = "apps.main.views.handler_404"

schema_view = get_schema_view(
    openapi.Info(
        title="Flipify API",
        default_version="v1",
        description="API Endpoints for the Flipify APP",
        terms_of_service="",  # Provide link to terms of service
        contact=openapi.Contact(email="backend@flipify.com"),
    ),
)

# All API Endpoints pertaining to the flipify api
# version one should be included here. no need to
# add `api/` it's already added in the `urlpatterns`
# all APIs can now be found at : http://127.0.0.1:8000/api/v1/
# API docs are at http://127.0.0.1:8000/api/v1/doc for
# swagger ui and http://127.0.0.1:8000/api/v1/redoc for
# redoc ui.
v1_endpoints = [
    path(
        "doc/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path("", include("apps.main.urls")),
    path("auth/", include("apps.authentication.urls")),
]


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include(v1_endpoints)),
]
