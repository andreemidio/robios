from django.contrib import admin

# Register your models here.
from apps.producao.models import Producao, Quantity, ParadasProducao


@admin.register(Producao)
class ProducaoProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'line', 'datetime_turn', 'parts_quantity', 'area_production', 'line_stops')
    search_fields = ('id', 'line', 'datetime_turn', 'parts_quantity', 'area_production', 'line_stops')


@admin.register(Quantity)
class QuantityProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'inicio', 'fim')
    search_fields = ('id', 'inicio', 'fim')


@admin.register(ParadasProducao)
class QuantityProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'mensagem', 'datetime')
    search_fields = ('id', 'mensagem', 'datetime')
