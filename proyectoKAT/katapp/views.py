from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.shortcuts import get_object_or_404
from .models import MLost, MFind, Aviso
from django.views.generic.edit import CreateView, UpdateView, DeleteView #Para crear, actualizar y eliminar elementos (CBV)
from django.urls import reverse_lazy #Modificar la vista para que redireccione correctamente al crear un elemento
from django.contrib.messages.views import SuccessMessageMixin #Importar para que salgan los mensajes
from .mixins import MLostMixin, MFindMixin, AvisoMixin #Importar nuestro mixin
from katapp.forms import MLostForm, MFindForm, AvisoForm #Importar los forms

from common.mixins import AreaRestringidaMixin #Importamos los mixins

#from django_filters.views import FilterView #Importar para filtrar las vistas
#from .filters import MLostFilter #Importar nuestro filtro

# Create your views here.
#!------------------------------------------ MASCOTAS PERDIDAS ---------------------------------------
class MPerdidaListView(TemplateView):
    template_name = "katapp/listado_m_perdidas.html"
    #filterset_class = MLostFilter
    #queryset = MLost.objects.all()

    def get_context_data(self, **kwargs):
        context = super(MPerdidaListView, self).get_context_data(**kwargs)
        
        # Obtener los valores de los filtros enviados por el usuario
        lugar_perdida = self.request.GET.get('lugar_perdida')
        tamano = self.request.GET.get('tamano')
        pelo = self.request.GET.get('pelo')
        
        #!PRUEBA PARA SACAR MÁS DE UN REGISTRO AL FILTRAR
        especie_id = kwargs.get('especie_id')
        color_id = kwargs.get('color_id')
        raza_id = kwargs.get('raza_id')

        # Obtener todas las mascotas
        mascotas = MLost.objects.all()

        # Filtrar los objetos de MLost utilizando los filtros recibidos

        if especie_id:
            # Filtrar por especie seleccionada
            mascotas = mascotas.filter(especie_id=especie_id)

        if color_id:
            # Filtrar por color seleccionado
            mascotas = mascotas.filter(color__id=color_id)

        if raza_id:
            # Filtrar por raza seleccionada
            mascotas = mascotas.filter(raza_id=raza_id)

        if lugar_perdida:
            # Filtrar por lugar_perdida escrito
            mascotas = mascotas.filter(lugar_perdida__icontains=lugar_perdida)
        if tamano:
            # Filtrar por tamaño escrito
            mascotas = mascotas.filter(tamano__icontains=tamano)
        if pelo:
            # Filtrar por pelo escrito
            mascotas = mascotas.filter(pelo__icontains=pelo)

        #context['lugar_perdida'] = lugar_perdida
        #context['tamano'] = tamano
        #context['pelo'] = pelo

        # Obtener todas las mascotas filtradas
        context['mascotas'] = mascotas

        return context
    
        #!CÓDIGO ANTES DE LOS FILTROS ----------------------------------
        '''filtro_id = kwargs.get('filtro_id')
        context['mascotas'] = MLost.objects.filter(id=filtro_id) if filtro_id else MLost.objects.all()
        return context'''
        #!CÓDIGO DESPUES DE LOS FILTROS ----------------------------------
        #context['filter_form'] = self.filterset.form # Utiliza la clave 'filter_form' 
        #return context
    '''def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.select_related('especie')
        queryset = queryset.prefetch_related('color', 'raza')

        selected_species = self.request.GET.get('especie')
        print("Valor seleccionado:", selected_species)

        # Aplicar filtros del formulario si están presentes en la URL (GET)
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        queryset = self.filterset.qs

        return queryset'''
'''def mperdida_list(request):
    f = MLostFilter(request.GET, queryset=MLost.objects.all())
    selected_species = request.GET.get('especie')
    print("Valor seleccionado:", selected_species)
    return render(request, 'katapp/listado_m_perdidas.html', {'filter': f})'''


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
class MLostCreateView(AreaRestringidaMixin, MLostMixin, CreateView):
    form_class = MLostForm
    success_message = "Mascota creada exitosamente"
    def get_success_message(self, cleaned_data):
        return self.success_message + ' - ' + str(self.object)

#!--------------------------------------- FORMULARIO MODIFICAR M_LOST -------------------------------------

class MLostUpdateView(AreaRestringidaMixin, MLostMixin, UpdateView):
    form_class = MLostForm
    def get_success_message(self, cleaned_data):
        return "Mascota '{}' actualizada exitosamente".format(str(self.object))
    #success_url = reverse_lazy('m_perdida')

#!----------------------------------------- FORMULARIO BORRAR M_LOST ---------------------------------------
class MLostDeleteView(AreaRestringidaMixin, DeleteView):
    model = MLost
    success_message = "Mascota borrada exitosamente"
    success_url = reverse_lazy('m_perdida')
    template_name = 'katapp/mlost_confirm_delete.html'

#!-------------------------------------------- FORMULARIOS M_FIND ------------------------------------------
class MFindCreateView(AreaRestringidaMixin, MFindMixin, CreateView):
    form_class = MFindForm
    success_message = "Mascota creada exitosamente"
    def get_success_message(self, cleaned_data):
        return self.success_message + ' - ' + str(self.object)

class MFindUpdateView(AreaRestringidaMixin, MFindMixin, UpdateView):
    form_class = MFindForm
    def get_success_message(self, cleaned_data):
        return "Mascota '{}' actualizada exitosamente".format(str(self.object))
    #success_url = reverse_lazy('m_perdida')

class MFindDeleteView(AreaRestringidaMixin, DeleteView):
    model = MLost
    success_url = reverse_lazy('m_encontrada')
    template_name = 'katapp/mfind_confirm_delete.html'

#!-------------------------------------------- FORMULARIOS AVISOS ------------------------------------------
class AvisoCreateView(AreaRestringidaMixin, AvisoMixin, CreateView):
    form_class = AvisoForm
    success_message = "Aviso creado exitosamente"
    def get_success_message(self, cleaned_data):
        return self.success_message + ' - ' + str(self.object)

class AvisoUpdateView(AreaRestringidaMixin, AvisoMixin, UpdateView):
    form_class = AvisoForm
    def get_success_message(self, cleaned_data):
        return "Aviso '{}' actualizado exitosamente".format(str(self.object))

class AvisoDeleteView(AreaRestringidaMixin, DeleteView):
    model = Aviso
    success_url = reverse_lazy('avisos')
    template_name = 'katapp/aviso_confirm_delete.html'

#!------------------------------------------ CONTACTO MASCOTA -----------------------------------------
class MPerdidaContactoView(AreaRestringidaMixin, TemplateView):
    template_name = "katapp/mascota_perdida_contacto.html"
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        c_lost_id = kwargs.get('id')
        context['mascota'] = MLost.objects.get(id=c_lost_id)
        return context
    
class MEncontradaContactoView(AreaRestringidaMixin, TemplateView):
    template_name = "katapp/mascota_encontrada_contacto.html"
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        c_find_id = kwargs.get('id')
        context['mascota'] = MFind.objects.get(id=c_find_id)
        return context