from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from rest_framework import routers
from locacao.views import ClientesViewSet

router = routers.DefaultRouter()

router.register(
    'clientes', ClientesViewSet, basename='clientes'
)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('',include('locacao.urls')),
    path('accounts/', include('django.contrib.auth.urls'), name='login'),
    path('api-auth/', include('rest_framework.urls')),
]
