from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.

class HomeView(TemplateView):
    template_name = 'common/home.html'

class PanelView(TemplateView):
    template_name = 'common/panel_inicio.html'
