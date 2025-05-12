"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import permissions
from apps.accounts.views import CustomLoginView, VerifyTokenView, CustomUserDetailsView


schema_view = get_schema_view(
    openapi.Info(
        title="Ehgz API",
        default_version="v1",
        description="API endpoints for Ehgz",
        contact=openapi.Contact(email="karsonziad@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    permission_classes=(permissions.AllowAny,),
    public=True,
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    # Auth
    path('api/auth/register/', include('dj_rest_auth.registration.urls')),
    path('api/auth/login/', CustomLoginView.as_view(), name='custom-login'),
    path('api/auth/token/verify/', VerifyTokenView.as_view(), name='verify-token'),
    path('api/auth/user/', CustomUserDetailsView.as_view(), name='user-details'),
    path('api/auth/', include('dj_rest_auth.urls')),

    # Apps
    path('api/events', include('apps.events.urls')),
    path('api/book/', include('apps.bookings.urls')),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
