from django.urls import include, path
from django.contrib import admin
from django.urls import re_path

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title='Blogs API',
        default_version='v1',
        description = 'Blogs API documentation.'
    ), 
    public=True,
    permission_classes = [permissions.AllowAny,],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('posts.urls')),
    path('auth/', include('rest_framework.urls')),
    path('auth/v1/rest-auth/', include('dj_rest_auth.urls')),
    path('auth/v1/rest-auth/register/', include('dj_rest_auth.registration.urls')),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
 

]