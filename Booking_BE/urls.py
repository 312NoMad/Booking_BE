from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny

from django.contrib import admin
from django.urls import path, include


def swagger_info():
    return openapi.Info(
        title="Your Project API",
        default_version='v1',
        description="API documentation for Your Project",
        contact=openapi.Contact(email="your-email@example.com"),
        license=openapi.License(name="MIT License"),
    )


schema_view = get_schema_view(
    swagger_info(), public=True, permission_classes=[AllowAny]
)
urlpatterns = [
    path("admin/", admin.site.urls),

    path("user/", include("apps.user.urls")),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
