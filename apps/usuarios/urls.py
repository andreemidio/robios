from django.urls import path

from apps.usuarios.views import UserCreate

app_name = 'usuarios'

urlpatterns = [
    # ...
    path('add/', UserCreate.as_view(), name='add'),

]
