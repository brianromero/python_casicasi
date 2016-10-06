from django.conf.urls import url
from . import views
from . import openPdf

urlpatterns = [
    # Filtros...
    url(r'^recargaDepa/$', views.recargaDepa),
    url(r'^recargaProv/(\d+)/(\d+)/$', views.recargaProv),
    url(r'^recargaDis/(\d+)/(\d+)/(\d+)/$', views.recargaDis),
    url(r'^recargaZona/(\d+)/$', views.recargaZona),

    #Segmentacion...
    url(r'^segrecargaTabla01/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/$', views.segrecargaTabla01),
    
    # Croquis...
    url(r'^crorecargaTabla01/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/$', views.crorecargaTabla01),
    url(r'^crorecargaTabla02/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/$', views.crorecargaTabla02),
    url(r'^getfiles/$', views.getfiles),
    url(r'^crodescargarPdf/(\d+)/(\d+)/(\d+)/$', openPdf.crodescargarPdf),
    url(r'^descargarPdfAux/(\d+)/(\d+)/(\d+)/$', openPdf.descargarPdfAux),
    url(r'^descargarPdf/(\d+)/(\d+)/(\d+)/$', openPdf.descargarPdf),

    # Legajo...
    url(r'^legajorecargaTabla/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/$', views.legajorecargaTabla),
    url(r'^generar_lote/(\d+)/(\d+)/(\d+)/$', views.generar_lote),
    
]
