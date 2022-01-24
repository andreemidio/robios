from rest_framework import renderers, permissions, parsers, mixins
from rest_framework.viewsets import GenericViewSet

from apps.producao.models import Producao, ParadasProducao
from apps.producao.serializers import PostProducaoSerializer, ListProducaoSerializer, PostParadasProducaoSerializer


class PostProducaoViewSet(mixins.CreateModelMixin, GenericViewSet):
    queryset = Producao.objects.all()
    serializer_class = PostProducaoSerializer
    renderer_classes = [renderers.JSONRenderer]
    parser_classes = (parsers.JSONParser,)
    permission_classes = (permissions.AllowAny,)


class ListProducaoViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = Producao.objects.all()
    serializer_class = ListProducaoSerializer
    renderer_classes = [renderers.JSONRenderer]
    parser_classes = (parsers.JSONParser,)
    permission_classes = (permissions.AllowAny,)


class PostParadaViewSet(mixins.CreateModelMixin, GenericViewSet):
    queryset = ParadasProducao.objects.all()
    serializer_class = PostParadasProducaoSerializer
    renderer_classes = [renderers.JSONRenderer]
    parser_classes = (parsers.JSONParser,)
    permission_classes = (permissions.AllowAny,)
