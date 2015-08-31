"""SICOT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from principal.views import *
from SICOT import settings

urlpatterns = [






    url(r'^$','django.contrib.auth.views.login',{'template_name': 'login.html'},name='login'),
    url(r'^cerrar/$','django.contrib.auth.views.logout_then_login',name='logout'),




    url(r'^reportes/producto/generar_pdf/$', IndexView.as_view(), name='reporteproducto'),
    url(r'^generar_pdf/$', generar_pdf, name='generar_pdf'),

    url(r'^reportes/producto/generar_pdforden/$', Index.as_view(), name='reporteorden'),
    url(r'^generar_pdforden/$', generar_pdforden, name='generar_pdforden'),

    url(r'^notificaciones/$',notificaciones,name='notificaciones'),

    url(r'^usuario/ingresarusuario/$',newUser_view.as_view(),name='ingresarusuario'),
    url(r'^usuario/modificarusuario/(?P<pk>\d+)/$',editUser_view.as_view(),name='modificarrusuario'),

    url(r'^orden/gestionarorden/imprimirinicial/(?P<id>.*)/$',imprimirordeninicial, name='imprimirordeninicial'),
    url(r'^orden/gestionarorden/imprimir/(?P<id>.*)/$',imprimirorden, name='imprimirorden'),


    url(r'^inventario/gestionarproducto/ingresarproducto/', ingresarproducto, name='ingresarproducto'),
    url(r'^inventario/ingresarcategoria/', ingresarcategoria, name='ingresarcategoria'),
    url(r'^inventario/ingresarcategoria1/', ingresarcategoria1, name='ingresarcategoria1'),
    url(r'^inventario/gestionarproveedor/ingresarproveedor/', ingresarproveedor, name='ingresarproveedor'),
    url(r'^inventario/gestionarproveedor/ingresarproveedor1/', ingresarproveedor1, name='ingresarproveedor1'),

    url(r'^usuario/perfilusuario/(?P<id>\d+)/$', perfilusuario, name='perfilusuario'),
    url(r'^usuario/modificarperfil/(?P<pk>\d+)/$', modificarperfil_view.as_view(), name='modificarperfil'),
    url(r'^orden/gestionarorden/ingresarorden/', ingresarorden, name='ingresarorden'),
    url(r'^orden/gestionarcliente/ingresarcliente/',ingresarcliente, name='ingresarcliente'),
    url(r'^orden/gestionarcliente/nuevocliente/',nuevocli, name='nuevocli'),

    url(r'^inventario/gestionarproducto/modificarproducto/(?P<id>\d+)/$',modificarproducto, name='modificarproducto'),
    url(r'^inventario/gestionarproveedor/modificarproveedor/(?P<id>\d+)/$',modificarproveedor, name='modificarproveedor'),
    url(r'^inventario/gestionarcategoria/modificarcategoria/(?P<id>\d+)/$',modificarcategoria, name='modificarcategoria'),
    url(r'^usuario/modificarusuario/(?P<pk>.*)/',modificarusuario, name='modificarusuario'),
    url(r'^orden/gestionarorden/modificarorden/(?P<id>\d+)/$',modificarorden, name='modificarorden'),
    url(r'^orden/gestionarcliente/modificarcliente/(?P<id>\d+)/$',modificarcliente, name='modificarcliente'),

    url(r'^inventario/gestionarproducto/buscarproducto/',buscarproducto, name='buscarproducto'),
    url(r'^inventario/gestionarproveedor/buscarproveedor/',buscarproveedor, name='buscarproveedor'),
    url(r'^inventario/gestionarcategoria/buscarcategoria/',buscarcategoria, name='buscarcategoria'),
    url(r'^orden/gestionarorden/buscarorden/',buscarorden, name='buscarorden'),
    url(r'^usuario/buscarusuario/',buscarusuario, name='buscarusuario'),


    url(r'^orden/gestionarcliente/buscarcliente/',buscarcliente, name='buscarcliente'),
    url(r'^orden/gestionarcliente/ordencliente/',ordencliente, name='ordencliente'),
    url(r'^orden/gestionarorden/ordenproducto/',ordenproducto, name='ordenproducto'),

    url(r'^inventario/gestionarproducto/',gestionarproducto, name='gestionarproducto'),
    url(r'^inventario/gestionarproveedor/',gestionarproveedor, name='gestionarproveedor'),
    url(r'^inventario/gestionarcategoria/',gestionarcategoria, name='gestionarcategoria'),
    url(r'^orden/gestionarorden/',gestionarorden, name='gestionarorden'),
    url(r'^orden/gestionarcliente/',gestionarcliente, name='gestionarcliente'),



    url(r'^orden/$', orden, name='orden'),
    url(r'^inventario/$', v_inventario, name='inventario'),
    url(r'^reporte/$', reporte, name='reporte'),
    url(r'^usuario/$', usuario, name='usuario'),
    url(r'^inicio/$', index_view, name='inicio'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),



    #url(r'^media/(?P<path>.*)$','django.views.static.serve',
     #   {'document_root':settings.MEDIA_ROOT,}),
]
