from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from .models import MLost, MFind, Aviso
from django.views.generic.edit import CreateView, UpdateView, DeleteView #Para crear, actualizar y eliminar elementos (CBV)
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin #Importar para que salgan los mensajes

# Create your views here.
#!------------------------------------------ MASCOTAS PERDIDAS ---------------------------------------
class MPerdidaListView(TemplateView):
    template_name = "katapp/listado_m_perdidas.html"
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        lost_id = kwargs.get('pk')
        context['mascotas'] = MLost.objects.filter(id=lost_id) if lost_id else MLost.objects.all()
        return context

#-------------------------------- Recuperar mascota al clickar en una mascota de Panel
def m_perdida_detail_view(request,pk):
    mascota_perdida = MLost.objects.get(pk=pk)
    context = {'mascota': mascota_perdida}
    return render(request,'katapp/detalle_mascota_perdida.html',context)

#-------------------------------- Incluir código para que no explote la aplicación cuando se introduzca un id no válido. Que devuelva la
    #-------------------------------- página 404 o el objeto
def mPerdidaView(request, pk):
    mascota = get_object_or_404(MLost, pk=pk)
    context = {'mascota': mascota}
    return render(request, 'katapp/listado_m_perdidas.html', context)


class MPerdidaDetailView(TemplateView):
    template_name = "katapp/detalle_mascota_perdida.html"
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        lost_id = kwargs.get('id')
        context['mascota'] = MLost.objects.get(id=lost_id)
        return context

#!--------------------------------------------- MASCOTAS ENCONTRADAS ---------------------------------------
class MEncontradaListView(TemplateView):
    template_name = "katapp/listado_m_encontradas.html"
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        find_id = kwargs.get('pk')
        context['mascotas'] = MFind.objects.filter(id=find_id) if find_id else MFind.objects.all()
        return context

#-------------------------------- Recuperar mascota al clickar en una mascota de Panel
def m_encontrada_detail_view(request,pk):
    mascota_encontrada = MFind.objects.get(pk=pk)
    context = {'mascota': mascota_encontrada}
    return render(request,'katapp/detalle_mascota_encontrada.html',context)

#-------------------------------- Incluir código para que no explote la aplicación cuando se introduzca un id no válido. Que devuelva la
    #-------------------------------- página 404 o el objeto
def mEncontradaView(request, pk):
    mascota = get_object_or_404(MFind, pk=pk)
    context = {'mascota': mascota}
    return render(request, 'katapp/listado_m_encontradas.html', context)


class MEncontradaDetailView(TemplateView):
    template_name = "katapp/detalle_mascota_encontrada.html"
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        find_id = kwargs.get('id')
        context['mascota'] = MFind.objects.get(id=find_id)
        return context

#!------------------------------------------------- AVISOS -----------------------------------------------
class AvisoListView(TemplateView):
    template_name = "katapp/listado_avisos.html"
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        aviso_id = kwargs.get('pk')
        context['avisos'] = Aviso.objects.filter(id=aviso_id) if aviso_id else Aviso.objects.all()
        return context

#-------------------------------- Recuperar mascota al clickar en una mascota de Panel
def aviso_detail_view(request,pk):
    aviso = Aviso.objects.get(pk=pk)
    context = {'aviso': aviso}
    return render(request,'katapp/detalle_aviso.html',context)

#-------------------------------- Incluir código para que no explote la aplicación cuando se introduzca un id no válido. Que devuelva la
    #-------------------------------- página 404 o el objeto
def avisoView(request, pk):
    aviso = get_object_or_404(Aviso, pk=pk)
    context = {'aviso': aviso}
    return render(request, 'katapp/listado_avisos.html', context)


class AvisoDetailView(TemplateView):
    template_name = "katapp/detalle_aviso.html"
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        aviso_id = kwargs.get('id')
        context['aviso'] = Aviso.objects.get(id=aviso_id)
        return context

#!----------------------------------------- FORMULARIO CREAR M_LOST ---------------------------------------
class MLostCreateView(SuccessMessageMixin, CreateView):
    model = MLost
    fields = ['nombre', 'especie', 'lugar_perdida', 'foto', 'descripcion', 'color', 'sexo', 'anio_nacimiento', 'raza', 'fecha_extravio', 'datos_contacto', 'tamano', 'peso', 'num_chip', 'pelo', 'collar', 'devuelto']
    success_message = "Mascota creada exitosamente"
    def get_success_message(self, cleaned_data):
        return self.success_message + ' - ' + str(self.object)
    #---------------------------- Modificar la vista para que redireccione correctamente al crear un proyecto
        #Reverse lazy hace que, mediante el nombre, obtengamos la estructura de la url que queremos redireccionar
    def get_success_url(self):
        object = self.object
        return reverse_lazy('m_perdida_update', kwargs={'pk': object.id})

#!--------------------------------------- FORMULARIO MODIFICAR  M_FIND -------------------------------------

class MLostUpdateView(SuccessMessageMixin, UpdateView):
    model = MLost
    fields = ['nombre', 'especie', 'lugar_perdida', 'foto', 'descripcion', 'color', 'sexo', 'anio_nacimiento', 'raza', 'fecha_extravio', 'datos_contacto', 'tamano', 'peso', 'num_chip', 'pelo', 'collar', 'devuelto']
    def get_success_message(self, cleaned_data):
        return "Mascota '{}' actualizada exitosamente".format(str(self.object))
    success_url = reverse_lazy('m_perdida')

#!----------------------------------------- FORMULARIO BORRAR M_FIND ---------------------------------------
class MLostDeleteView(DeleteView):
    model = MLost
    success_url = reverse_lazy('m_perdida')
    template_name = 'katapp/mlost_confirm_delete.html'
