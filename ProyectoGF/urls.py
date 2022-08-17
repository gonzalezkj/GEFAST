"""ProyectoGF URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from AppArticulos.api.router import router_articulos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('AppBase.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', include('AppPerfiles.urls')),
    path('factura/', include('AppFactura.urls')),
    path('facturaventa/', include('AppFacturaV.urls')),
    path('nota/', include('AppNota.urls')),
    path('stock/', include('AppStock.urls')),
    path('reportes/', include('AppReportes.urls')),
    path('registros/', include('AppRegistros.urls')),
    path('clientes/', include('AppClientes.urls')),
    path('articulos/', include('AppArticulos.urls')),
    path('agregar/', include('AppAgregar.urls')),
    path('agregarv/', include('AppAgregarV.urls')),
    path('agregarcli/', include('AppAgregarCli.urls')),
    path('agregarprov/', include('AppAgregarProv.urls')),
    path('agregarf/', include('AppAgregarF.urls')),
    path('agregarfv/', include('AppAgregarFV.urls')),
    path('abm/', include('AppABM.urls')),
    path('cuentacorriente/', include('AppCC.urls')),
    path('api/', include(router_articulos.urls)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
