from rest_framework import serializers

from apps.producao.models import Producao, Quantity


class PostQuantitySerializers(serializers.ModelSerializer):
    inicio = serializers.DateTimeField(format="%d/%m/%Y %H:%M:%S")
    fim = serializers.DateTimeField(format="%d/%m/%Y %H:%M:%S")

    class Meta:
        model = Quantity
        fields = ['inicio', 'fim']


class PostProducaoSerializer(serializers.ModelSerializer):
    quantity = PostQuantitySerializers(many=True)

    class Meta:
        model = Producao
        fields = '__all__'

    def create(self, validated_data):
        quantity = validated_data.pop('quantity', {})

        producao = Producao.objects.create(**validated_data)

        for q in quantity:
            quantidade = Quantity.objects.create(**q)

        return validated_data


class ListProducaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producao
        fields = '__all__'
