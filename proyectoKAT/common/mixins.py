#*UD8.3 Realizamos las importaciones
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

#Creamos un mixin para no repetir código en cada vista.
class AreaRestringidaMixin():
    @method_decorator(login_required)
    #Sobreescribimos el método dispatch
    def dispatch(self, request, *args, **kwargs):
        #Si el user no está autenticado, lo redirigirá a la pantalla de login
        if not request.user.is_authenticated:
            return redirect("login")
        return super().dispatch(request, *args, **kwargs)