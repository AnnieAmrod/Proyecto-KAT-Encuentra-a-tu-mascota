from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import MLost, MFind, Aviso
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, HTML, Field, Row


class MLostForm(forms.ModelForm):
    descripcion = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = MLost
        fields = ['nombre', 'especie', 'lugar_perdida', 'foto', 'descripcion', 'color', 'sexo', 'anio_nacimiento', 'raza', 'fecha_extravio', 'datos_contacto', 'tamano', 'peso', 'num_chip', 'pelo', 'collar', 'devuelto']

class MFindForm(forms.ModelForm):
    descripcion = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = MFind
        fields = ['nombre', 'especie', 'lugar_encontrado', 'foto', 'descripcion', 'color', 'sexo', 'raza', 'fecha_encontrado', 'datos_contacto', 'tamano', 'num_chip', 'pelo', 'collar', 'devuelto']

class AvisoForm(forms.ModelForm):
    #descripcion = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Aviso
        fields = ['razon', 'tipo_aviso', 'fecha_aviso', 'hora_aviso', 'ubicacion', 'provincia', 'ciudad', 'imagen', 'descripcion', 'contacto']
    def __init__(self, *args, **kwargs):
        super(AvisoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Row(
                Div(
                    Div(Field('razon'), css_class="mb-4"),
                    Div(Field('tipo_aviso'), css_class="mb-4"),
                    Row(
                    Div(Field('fecha_aviso'), css_class="col-6 mb-3"),
                    Div(Field('hora_aviso'), css_class="col-6 mb-3"),
                    ),
                    css_class="col-6"
                ),
                Div(Field('descripcion'), css_class="col-6"),
            ),
            HTML('<hr>'),
            Row( #De esta forma no tendremos que usar la clase row
                Div(Field('ubicacion'), css_class="col-4"),
                Div(Field('provincia'), css_class="col-4"),
                Div(Field('ciudad'), css_class="col-4"),
                #css_class="row"
            ),
            HTML('<hr>'),
            Div(
                Field('imagen'),
                Field('contacto', css_class="mb-3"),
                css_class="mb-5"
            ),
        )