import os
import uuid

from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models


# Create your models here.



def get_file_path(filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('usuario_assinatura', filename)


class EmailUserManager(BaseUserManager):
    def create_user(self, *args, **kwargs):
        email = kwargs["email"]
        email = self.normalize_email(email)
        password = kwargs["password"]
        kwargs.pop("password")

        if not email:
            raise ValueError('Necessário um email válido')

        user = self.model(**kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, *args, **kwargs):
        user = self.create_user(**kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class Usuarios(AbstractBaseUser, PermissionsMixin):
    nome_sobrenome = models.CharField(max_length=255, blank=True, null=True)
    cpf = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(unique=True, max_length=255)
    reset_password = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False, blank=True, null=True)
    is_staff = models.BooleanField(default=False, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    objects = EmailUserManager()

    def __str__(self):
        return self.email

    def __repr__(self):
        return self.email

    @property
    def ativo_human(self):
        return 'Sim' if self.is_active else 'Não'

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        db_table = 'usuarios'
        ordering = ['-data_criacao']
