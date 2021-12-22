from django.db import models


# Create your models here.

class Producao(models.Model):
    line = models.IntegerField(null=True)
    datetime_turn = models.DateTimeField(auto_now_add=True)
    parts_quantity = models.IntegerField()
    area_production = models.FloatField()
    line_stops = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

    def __repr__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Producao'
        verbose_name_plural = 'Producoes'
        db_table = 'producao'
        # ordering = ['id']


class Quantity(models.Model):
    inicio = models.DateTimeField(null=True)
    fim = models.DateTimeField(null=True)
    producao = models.ManyToManyField(Producao)


    def __str__(self):
        return str(self.id)

    def __repr__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'quantity'
        verbose_name_plural = 'quantities'
        db_table = 'quantity'
        # ordering = ['-inicio']

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
