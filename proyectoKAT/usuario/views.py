from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.views import View
from usuario.forms import UsuarioRegistradoForm
from django.views.generic.edit import UpdateView
from .models import Usuario
from common.mixins import AreaRestringidaMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

# Create your views here.
#* Creamos la clase LoginFormView
class LoginFormView(LoginView):
    template_name = '../templates/usuario/login.html'

    #* Sobreescribimos el método get_context_data para cambiar su título
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['titulo'] = "Iniciar sesión"
        return context

class UsuarioRegistradoUpdateView(AreaRestringidaMixin, SuccessMessageMixin, UpdateView):
    form_class = UsuarioRegistradoForm
    model = Usuario
    def get_success_message(self, cleaned_data):
        return "Usuario '{}' actualizado exitosamente".format(str(self.object))
    #---------------------------- Modificar la vista para que redireccione correctamente al crear un proyecto
        #Reverse lazy hace que, mediante el nombre, obtengamos la estructura de la url que queremos redireccionar
    def get_success_url(self):
        object = self.object
        return reverse_lazy('usuario_registrado_update', kwargs={'pk': object.id})