from django import forms
from .models import Usuario
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, HTML, Field, Row



class UsuarioRegistradoForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['email', 'nombre', 'apellido1', 'apellido2', 'direccion', 'telefono', 'cod_postal', 'ciudad', 'provincia']
    def __init__(self, *args, **kwargs):
        super(UsuarioRegistradoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Row(
                Div(
                    Div(Field('nombre'), css_class="mb-4"),
                    Row(
                    Div(Field('apellido1'), css_class="col-6 mb-3"),
                    Div(Field('apellido2'), css_class="col-6 mb-3"),
                    ),
                    css_class="col-6"
                ),
                Div(
                    Div(Field('email'), css_class="mb-4"),
                    Div(Field('telefono'), css_class="mt-5 mt-md-0 mb-3"),
                    css_class="col-6"
                ),
            ),
            HTML('<hr>'),
            Row( #De esta forma no tendremos que usar la clase row
                Div(Field('ciudad'), css_class="col-6"),
                Div(Field('cod_postal'), css_class="col-6"),
                Div(Field('provincia'), css_class="col-6"),
                Div(Field('direccion'), css_class="col-6"),
                #css_class="row"
            ),

        )