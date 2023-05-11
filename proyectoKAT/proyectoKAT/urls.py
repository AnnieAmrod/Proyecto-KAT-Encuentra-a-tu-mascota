"""proyectoKAT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from common import views as common_views
from katapp import views as  katapp_views

urlpatterns = [
path('admin/', admin.site.urls),
path('', common_views.HomeView.as_view(), name='home'),
path('home/', common_views.HomeView.as_view(), name='home'),
path('panel/', common_views.PanelView.as_view(), name='panel'),
path('m_perdida/', katapp_views.MPerdidaListView.as_view(), name='m_perdida'),
path('m_perdidadetail/<int:id>/', katapp_views.MPerdidaDetailView.as_view(), name='m_perdidadetail'),
path('m_encontrada/', katapp_views.MEncontradaListView.as_view(), name='m_encontrada'),
path('m_encontradadetail/<int:id>/', katapp_views.MEncontradaDetailView.as_view(), name='m_encontradadetail'),
path('aviso/', katapp_views.AvisoListView.as_view(), name='aviso'),
path('avisodetail/<int:id>/', katapp_views.AvisoDetailView.as_view(), name='avisodetail'),
path('conocenos', common_views.ConocenosView.as_view(), name='conocenos'),
path('m_perdida_create/', katapp_views.MLostCreateView.as_view(), name='m_perdida_create'), #Para crear elementos (CBV)
path('m_perdida_update/<int:pk>/', katapp_views.MLostUpdateView.as_view(), name='m_perdida_update'),
path('m_perdida_delete/<int:pk>/', katapp_views.MLostDeleteView.as_view(), name='m_perdida_delete'),
]

if settings.DEBUG: urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

