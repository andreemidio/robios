from django.urls import path, include
from rest_framework import routers

from apps.producao.viewsets import PostProducaoViewSet, ListProducaoViewSet

app_name = 'producao'

router = routers.DefaultRouter()

router.register(r'criar', PostProducaoViewSet, basename='criar-producao')
router.register(r'listar', ListProducaoViewSet, basename='listar-producao')

urlpatterns = [

    path(r'', include(router.urls)),

]
