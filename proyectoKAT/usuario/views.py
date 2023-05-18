from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.views import View

# Create your views here.
#* Creamos la clase LoginFormView
class LoginFormView(LoginView):
    template_name = '../templates/usuario/login.html'

    #* Sobreescribimos el método get_context_data para cambiar su título
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['titulo'] = "Iniciar sesión"
        return context