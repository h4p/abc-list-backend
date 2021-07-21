import abclist.views
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from django.contrib import admin

admin.autodiscover()


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('abclist.urls')),

    # Path to obtain a new access and refresh token
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
