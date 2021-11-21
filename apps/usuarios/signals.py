from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.v1.usuarios.models import Usuarios


@receiver(post_save, sender=Usuarios)
def send_email_create(sender, *args, **kwargs):
    pass
