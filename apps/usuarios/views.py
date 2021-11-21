# Create your views here.
from django.views.generic import CreateView

from apps.usuarios.models import Usuarios


class UserCreate(CreateView):
    model = Usuarios
    fields = '__all__'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
