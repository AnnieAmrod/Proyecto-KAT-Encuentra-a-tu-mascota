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
from usuario import views as usuario_views
from usuario.views import LoginFormView, LogoutView
from django.urls import include
from django_filters.views import FilterView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', common_views.HomeView.as_view(), name='home'),
    path('home/', common_views.HomeView.as_view(), name='home'),
    path('panel/', common_views.PanelView.as_view(), name='panel'),

    path('m_perdida/', katapp_views.MPerdidaListView.as_view(), name='m_perdida'),
    path('m_perdida/<int:filtro_id>/', katapp_views.MPerdidaListView.as_view(), name='m_perdida'),
    #path('m_perdida/', katapp_views.mperdida_list, name="m_perdida"),
    #path('m_perdida/', katapp_views.FilterView.as_view(model=katapp_views.MPerdidaListView), name='m_perdida'),
    path('m_perdidadetail/<int:id>/', katapp_views.MPerdidaDetailView.as_view(), name='m_perdidadetail'),

    path('m_perdida_create/', katapp_views.MLostCreateView.as_view(), name='m_perdida_create'), #Para crear elementos (CBV)
    path('m_perdida_update/<int:pk>/', katapp_views.MLostUpdateView.as_view(), name='m_perdida_update'),
    path('m_perdida_delete/<int:pk>/', katapp_views.MLostDeleteView.as_view(), name='m_perdida_delete'),

    path('m_encontrada/', katapp_views.MEncontradaListView.as_view(), name='m_encontrada'),
    path('m_encontradadetail/<int:id>/', katapp_views.MEncontradaDetailView.as_view(), name='m_encontradadetail'),

    path('m_encontrada_create/', katapp_views.MFindCreateView.as_view(), name='m_encontrada_create'), #Para crear elementos (CBV)
    path('m_encontrada_update/<int:pk>/', katapp_views.MFindUpdateView.as_view(), name='m_encontrada_update'),
    path('m_encontrada_delete/<int:pk>/', katapp_views.MFindDeleteView.as_view(), name='m_encontrada_delete'),

    path('aviso/', katapp_views.AvisoListView.as_view(), name='aviso'),
    path('avisodetail/<int:id>/', katapp_views.AvisoDetailView.as_view(), name='avisodetail'),

    path('aviso_create/', katapp_views.AvisoCreateView.as_view(), name='aviso_create'), #Para crear elementos (CBV)
    path('aviso_update/<int:pk>/', katapp_views.AvisoUpdateView.as_view(), name='aviso_update'),
    path('aviso_delete/<int:pk>/', katapp_views.AvisoDeleteView.as_view(), name='aviso_delete'),

    path('conocenos/', common_views.ConocenosView.as_view(), name='conocenos'),

    path('login/', LoginFormView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page="login"), name="logout"),

    path('accounts/', include('allauth.urls')),

    path('m_perdida_contacto/<int:id>/', katapp_views.MPerdidaContactoView.as_view(), name='m_perdida_contacto'),
    path('m_encontrada_contacto/<int:id>/', katapp_views.MEncontradaContactoView.as_view(), name='m_encontrada_contacto'),

    path('usuario_registrado_update/<int:pk>/', usuario_views.UsuarioRegistradoUpdateView.as_view(), name='usuario_registrado_update'),

]

if settings.DEBUG: urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

