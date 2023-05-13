from django.contrib.messages.views import SuccessMessageMixin
from .models import MLost, MFind, Aviso
from django.urls import reverse_lazy


class MLostMixin(SuccessMessageMixin):
    model = MLost
    #fields = ['nombre', 'especie', 'lugar_perdida', 'foto', 'descripcion', 'color', 'sexo', 'anio_nacimiento', 'raza', 'fecha_extravio', 'datos_contacto', 'tamano', 'peso', 'num_chip', 'pelo', 'collar', 'devuelto']
    #---------------------------- Modificar la vista para que redireccione correctamente al crear un proyecto
        #Reverse lazy hace que, mediante el nombre, obtengamos la estructura de la url que queremos redireccionar
    def get_success_url(self):
        object = self.object
        return reverse_lazy('m_perdida_update', kwargs={'pk': object.id})

class MFindMixin(SuccessMessageMixin):
    model = MFind
    #fields = ['nombre', 'especie', 'lugar_encontrado', 'foto', 'descripcion', 'color', 'sexo', 'raza', 'fecha_encontrado', 'datos_contacto', 'tamano', 'num_chip', 'pelo', 'collar', 'devuelto']
    #---------------------------- Modificar la vista para que redireccione correctamente al crear un proyecto
        #Reverse lazy hace que, mediante el nombre, obtengamos la estructura de la url que queremos redireccionar
    def get_success_url(self):
        object = self.object
        return reverse_lazy('m_encontrada_update', kwargs={'pk': object.id})

class AvisoMixin(SuccessMessageMixin):
    model = Aviso
    #---------------------------- Modificar la vista para que redireccione correctamente al crear un proyecto
        #Reverse lazy hace que, mediante el nombre, obtengamos la estructura de la url que queremos redireccionar
    def get_success_url(self):
        object = self.object
        return reverse_lazy('aviso_update', kwargs={'pk': object.id})