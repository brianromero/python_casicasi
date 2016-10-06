# coding=utf-8

from django.http import HttpResponse
from .models import Departamento, Provincia, Distrito, Zona
import json
from django.db.models import Count

# Croquis y listado...
import os
import zipfile
import StringIO

from urllib2 import Request, urlopen
from pyPdf import PdfFileWriter, PdfFileReader

# Legajos...
from io import BytesIO
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.pagesizes import A4
from reportlab.graphics.barcode import code39

# Filtros...
def recargaDepa(request):
    filtroDepa = Departamento.objects.filter(ccdd='02').values('ccdd','departamento').annotate(data=Count('ccdd')) | Departamento.objects.filter(ccdd='11').values('ccdd','departamento').annotate(data=Count('ccdd')) | Departamento.objects.filter(ccdd='24').values('ccdd','departamento').annotate(data=Count('ccdd'))
    data = list(filtroDepa)
    return HttpResponse(json.dumps(data), content_type='application/json')

"""def recargaDepa(request):
    dataAux = dataDepa()
    return HttpResponse(json.dumps(dataAux), content_type='application/json')

def dataDepa():    
    from django.db import connection
    cursor = connection.cursor()
    cursor.execute('exec ActualizaDepa %s,%s,%s,%s,%s', ('0','0','0','0','0') )
    print cursor
    columns = [column[0] for column in cursor.description]
    menu = []
    for row in cursor.fetchall():
        menu.append(dict(zip(columns, row)))"""

def recargaProv(request, depa, prov):
    filtroPro = Provincia.objects.filter(ccdd=depa, ccpp='01').values('ccpp','provincia').annotate(data=Count('ccdd','ccpp')) | Provincia.objects.filter(ccdd=depa, ccpp='02').values('ccpp','provincia').annotate(data=Count('ccdd','ccpp')) | Provincia.objects.filter(ccdd=depa, ccpp='18').values('ccpp','provincia').annotate(data=Count('ccdd','ccpp')) | Provincia.objects.filter(ccdd=depa,ccpp='06').values('ccpp','provincia').annotate(data=Count('ccdd','ccpp')) 
    data = list(filtroPro)
    return HttpResponse(json.dumps(data), content_type='application/json')

"""def recargaProv(request, depa, prov):
    dataAux = dataProv(depa,prov)
    return HttpResponse(json.dumps(dataAux), content_type='application/json')

def dataProv(depa, prov):    
    from django.db import connection
    cursor = connection.cursor()
    cursor.execute('exec ActualizaProv %s,%s,%s,%s,%s', (depa,prov,0,0,0) )
    print cursor
    columns = [column[0] for column in cursor.description]
    menu = []
    for row in cursor.fetchall():
        menu.append(dict(zip(columns, row)))"""

def recargaDis(request, depa, prov, dis):
    filtroDist = Distrito.objects.filter(ccdd=depa, ccpp=prov).values('ccdi','distrito').annotate(data=Count('ccpp','ccdi'))
    #filtroDist = [definition.encode("utf8") for definition in Distrito.objects.filter(ccdd=depa, ccpp=prov).values('ccdi','distrito').annotate(data=Count('ccpp','ccdi'))]
    data = list(filtroDist)
    return HttpResponse(json.dumps(data), content_type='application/json')

"""def recargaDis(request, depa, prov, dis):
    dataAux = dataDis(depa,prov,dis)
    return HttpResponse(json.dumps(dataAux), content_type='application/json')

def dataDis(depa, prov, dis):    
    from django.db import connection
    cursor = connection.cursor()
    cursor.execute('exec ActualizaDis %s,%s,%s,%s,%s', (depa,prov,dis,0,0) )
    print cursor
    columns = [column[0] for column in cursor.description]
    menu = []
    for row in cursor.fetchall():
        menu.append(dict(zip(columns, row)))"""

def recargaZona(request, ubigeo):
    print "ubigeo"
    print ubigeo
    filtroZona = Zona.objects.filter(ubigeo='240106').values('ubigeo','zona').annotate(data=Count('ubigeo'))
    data = list(filtroZona)
    print(filtroZona)
    return HttpResponse(json.dumps(data), content_type='application/json')

"""def recargaZona(request, ubigeo):
    dataAux = dataZona(depa,prov,dis)
    return HttpResponse(json.dumps(dataAux), content_type='application/json')

def dataZona(ubigeo):    
    from django.db import connection
    cursor = connection.cursor()
    cursor.execute('exec ActualizaZona %s,%s,%s,%s,%s', (ubigeo,0,0,0,0) )
    print cursor
    columns = [column[0] for column in cursor.description]
    menu = []
    for row in cursor.fetchall():
        menu.append(dict(zip(columns, row)))"""

# Segmentacion...
def segrecargaTabla01(request, tipo, ccdd, ccpp, ccdi, zona):
    dataAux = dataSeg(tipo, ccdd, ccpp, ccdi, zona)
    return HttpResponse(json.dumps(dataAux), content_type='application/json')

def dataSeg(tipo, ccdd, ccpp, ccdi, zona):    
    from django.db import connection
    cursor = connection.cursor()
    cursor.execute('exec ActualizaTablaSeg %s,%s,%s,%s,%s', (tipo,ccdd,ccpp,ccdi,zona) )
    print cursor
    columns = [column[0] for column in cursor.description]
    menu = []
    for row in cursor.fetchall():
        menu.append(dict(zip(columns, row)))
    return menu

# Croquis y listado...
def crorecargaTabla01(request, tipo, ccdd, ccpp, ccdi, zona):
    dataAux = dataCro(tipo, ccdd, ccpp, ccdi, zona)
    return HttpResponse(json.dumps(dataAux), content_type='application/json')

def dataCro(tipo, ccdd, ccpp, ccdi, zona):    
    from django.db import connection
    cursor = connection.cursor()
    cursor.execute('exec ActualizaTablaCro %s,%s,%s,%s,%s', (tipo,ccdd,ccpp,ccdi,zona) )
    print cursor
    columns = [column[0] for column in cursor.description]
    menu = []
    for row in cursor.fetchall():
        menu.append(dict(zip(columns, row)))
    return menu    

def crorecargaTabla02(request, tipo, ccdd, ccpp, ccdi, zona):
    dataAux = dataCroquis(tipo, ccdd, ccpp, ccdi, zona)
    return HttpResponse(json.dumps(dataAux), content_type='application/json')

def dataCroquis(tipo, ccdd, ccpp, ccdi, zona):    
    from django.db import connection
    cursor = connection.cursor()
    cursor.execute('exec ActualizaPopCroquis %s,%s,%s,%s,%s', (tipo,ccdd,ccpp,ccdi,zona) )
    print cursor
    columns = [column[0] for column in cursor.description]
    menu = []
    for row in cursor.fetchall():
        menu.append(dict(zip(columns, row)))
    return menu

def getfiles(request):
    filenames = ["http://192.168.221.123/desarrollo/020601001000011.pdf","http://192.168.221.123/desarrollo/020601001000011.pdf"]
    zip_subdir = "somefiles"
    zip_filename = "%s.zip" % zip_subdir
    s = StringIO.StringIO()
    zf = zipfile.ZipFile(s, "w")
    for fpath in filenames:
        fdir, fname = os.path.split(fpath)
        zip_path = os.path.join(zip_subdir, fname)
        zf.write(fpath, zip_path)
    zf.close()
    resp = HttpResponse(s.getvalue(), mimetype = "application/x-zip-compressed")
    resp['Content-Disposition'] = 'attachment; filename=%s' % zip_filename
    return resp
    
# Legajo...
def legajorecargaTabla(request, tipo, ccdd, ccpp, ccdi, zona, distri):
    dataAux = dataLegajo(tipo, ccdd, ccpp, ccdi, zona, distri)
    return HttpResponse(json.dumps(dataAux), content_type='application/json')

def dataLegajo(tipo, ccdd, ccpp, ccdi, zona, distri):    
    from django.db import connection
    cursor = connection.cursor()
    cursor.execute('exec ActualizaLegajo %s,%s,%s,%s,%s,%s', (tipo,ccdd,ccpp,ccdi,zona,distri) )
    print cursor
    columns = [column[0] for column in cursor.description]
    menu = []
    for row in cursor.fetchall():
        menu.append(dict(zip(columns, row)))
    return menu

def generarEtiqueta(request, ubigeo, zona, tipo):
    
    """from django.db import connection
    cursor = connection.cursor()
    cursor.execute('exec ObtenerEtiqueta %s,%s,%s', (ubigeo,zona,tipo) )
    print cursor
    columns = [column[0] for column in cursor.description]
    menu = []
    for row in cursor.fetchall():
        menu.append(dict(zip(columns, row)))"""
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = "attachment; filename="+ubigeo+".pdf"
    buff = BytesIO()
    doc = SimpleDocTemplate(buff, pagesize=A4, rightMargin=70, leftMargin=70, topMargin=60, bottomMargin=18,)
    story = []
    string = ubigeo
    st = code39.Extended39(string)
    story.append(st)        
    doc.build(story)
    response.write(buff.getvalue())
    buff.close()
    return response

def generar_lote(request, ubigeo, zona, tipo):
    zona = Zona.objects.filter(ubigeo=ubigeo)
    total = int(str(Zona.objects.filter(ubigeo='020601').count()))
    list =[]
    for aeu in range(total):
         list.append(aeu + 1)
         generarEtiqueta(request,ubigeo,zona,tipo)
    return HttpResponse(list)
