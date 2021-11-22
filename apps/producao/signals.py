from django.db.models.signals import pre_save
from django.dispatch import receiver

from apps.producao.models import Quantity


@receiver(pre_save, sender=Quantity)
def my_callback(sender, instance, *args, **kwargs):
    instance.resultado =  instance.fim * instance.inicio
