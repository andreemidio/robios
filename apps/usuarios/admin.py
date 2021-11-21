from django.contrib import admin

# Register your models here.
from apps.usuarios.models import Usuarios


@admin.register(Usuarios)
class UsuariosProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_sobrenome', 'cpf', 'email',)
    search_fields = ('id', 'nome_sobrenome', 'cpf', 'email',)
