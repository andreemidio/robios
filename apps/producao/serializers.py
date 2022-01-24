from rest_framework import serializers

from apps.producao.models import Producao, Quantity, ParadasProducao


class PostQuantitySerializers(serializers.ModelSerializer):
    inicio = serializers.DateTimeField(format="%d/%m/%Y %H:%M:%S")
    fim = serializers.DateTimeField(format="%d/%m/%Y %H:%M:%S")

    class Meta:
        model = Quantity
        fields = ['inicio', 'fim']


class PostProducaoSerializer(serializers.ModelSerializer):
    stops_quantity = PostQuantitySerializers(many=True)

    class Meta:
        model = Producao
        fields = ['line', 'parts_quantity', 'area_production', 'line_stops','stops_quantity']

    def create(self, validated_data):
        try:
            retorno = validated_data.copy()

            stops_quantity = validated_data.pop('stops_quantity')

            producao = Producao.objects.create(**validated_data)

            for q in stops_quantity:
                quantidade = Quantity.objects.create(**q)
                quantidade.producao.add(producao)

            return retorno

        except Exception as e:
            raise serializers.ValidationError({'detail': e})


class PostParadasProducaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParadasProducao
        fields = ['mensagem']


class ListProducaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producao
        fields = '__all__'
