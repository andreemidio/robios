from rest_framework import renderers, permissions, parsers, mixins
from rest_framework.viewsets import GenericViewSet

from apps.producao.models import Producao
from apps.producao.serializers import PostProducaoSerializer, ListProducaoSerializer


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
