from django.contrib import admin

# Register your models here.
from apps.producao.models import Producao, Quantity


@admin.register(Producao)
class ProducaoProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'line', 'datetime_turn', 'parts_quantity', 'area_production', 'line_stops')
    search_fields = ('id', 'line', 'datetime_turn', 'parts_quantity', 'area_production', 'line_stops')


@admin.register(Quantity)
class QuantityProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'inicio', 'fim', 'producao')
    search_fields = ('id', 'inicio', 'fim', 'producao')
