from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('apps.portal.urls')),
    path('api/', include('apps.api.urls')),
    path('auth/', include('apps.auth.urls')),
    path('admin/', include('apps.admin.urls')),
    path('_/', admin.site.urls),
]
