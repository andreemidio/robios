from django.db import models


# Create your models here.


class Producao(models.Model):
    line = models.IntegerField(null=True)
    datetime_turn = models.DateTimeField()
    parts_quantity = models.IntegerField()
    area_production = models.FloatField()
    line_stops = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.line} | {self.parts_quantity}"

    def __repr__(self):
        return f"{self.line} | {self.parts_quantity}"

    class Meta:
        verbose_name = 'Producao'
        verbose_name_plural = 'Producoes'
        ordering = ['-id']


class Quantity(models.Model):
    inicio = models.DateTimeField()
    fim = models.DateTimeField()
    producao = models.ForeignKey(Producao, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.inicio} | {self.fim}"

    def __repr__(self):
        return f"{self.inicio} | {self.fim}"

    class Meta:
        verbose_name = 'Quantity'
        verbose_name_plural = 'Quantities'
        ordering = ['-inicio']


# {
#   "idProduction": 0,
#   "datetime_turn": "2021-10-29 16:51:00",
#   "PartsQuantity": 20,
#   "AreaProduction": 0, #area/min
#   "Line_Stops": True,
#   "Quantity": [
#     {
#       "inicio": "2021-10-29 16:41:00",
#       "fim": "2021-10-29 16:41:20"
#     }
#   ],
# }
