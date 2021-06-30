import abclist.views
from django.urls import path, include
from rest_framework import routers
from django.contrib import admin

admin.autodiscover()


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('abclist.urls')),
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
