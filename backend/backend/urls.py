
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api_auth/',include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('',include('core.urls')),
    path('rest-auth/',include('rest_auth.urls')),
    path('rest-auth/registration/',include('rest_auth.registration.urls')),
]
