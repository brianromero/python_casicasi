from django.http import HttpResponse
from urllib2 import Request, urlopen
from pyPdf import PdfFileWriter, PdfFileReader
from StringIO import StringIO
from .models import Departamento
from django.db.models import Count
import json
import zipfile
import os
import StringIO
import urllib2
from .models import Zona, TablaAeu 

def descargarPdf(request,ubigeo,zona,tipo):
    lista = []
    dataAux = dataZip(ubigeo,zona,tipo)
    print dataAux
    for pdf in dataAux:
        if tipo == '1':
            ubigeo="020601"
            zona="00100"
            ruta = "http://192.168.221.123/desarrollo/"+ubigeo+zona+"00"+str(pdf.get("SECCION",None))+".pdf"
            nombrePdf = ubigeo+zona+"00"+str(pdf.get("SECCION",None))+".pdf"
            lista.append(nombrePdf)
            download_url=ruta
            response = urllib2.urlopen(download_url)
            # validar cuando la seccion es mayor a 9
            file = open(ubigeo+zona+"00"+str(pdf.get("SECCION", None))+".pdf", 'wb')      
        if tipo == '2':
            ubigeo="020601"
            zona="00100"
            ruta = "http://192.168.221.123/desarrollo/"+ubigeo+zona+"00"+str(pdf.get("SECCION",None))+str(pdf.get("AEU",None))+".pdf"
            nombrePdf = ubigeo+zona+"00"+str(pdf.get("SECCION",None))+str(pdf.get("AEU",None))+".pdf"
            lista.append(nombrePdf)
            print "ruta: "+ruta
            download_url=ruta
            response = urllib2.urlopen(download_url)
            # validar cuando la seccion es mayor a 9
            file = open(ubigeo+zona+"00"+str(pdf.get("SECCION", None))+str(pdf.get("AEU",None))+".pdf", 'wb')
        file.write(response.read())
        file.close()
    s = descargarPdfAux(lista)
    resp = HttpResponse(s.getvalue(), content_type='application/zip')
    if tipo == '1':
        resp['Content-Disposition']='attachment; filename=seccion.zip'
    else:
        resp['Content-Disposition']='attachment; filename=aeu.zip'
    return resp

def dataZip(ubigeo, zona, tipo):    
    from django.db import connection
    cursor = connection.cursor()
    #cursor.execute('exec ListaZip %s,%s,%s', (ubigeo,zona,tipo) )
    cursor.execute('exec ListaZip %s,%s,%s', ('021806','00100',2) )
    columns = [column[0] for column in cursor.description]
    menu = []
    for row in cursor.fetchall():
        menu.append(dict(zip(columns, row)))
    return menu

def descargarPdfAux(lista):
    #filenames_url = ['02060100100001.pdf','02060100100001.pdf']
    #s = StringIO.StringIO()
    #zf = zipfile.ZipFile(s,"w")
    #zf.write('02060100100001.pdf')
    filenames_url = lista
    s = StringIO.StringIO()
    zf = zipfile.ZipFile(s,"w")
    print filenames_url
    for file_url in filenames_url:
        print "nombre del pdf: "+file_url
        zf.write(file_url)          
    zf.close()
    return s

def crodescargarPdf(request,ubigeo,zona,tipo):
    url = "http://192.168.221.123/desarrollo/020601001000011.pdf"
    writer = PdfFileWriter()
    remoteFile = urlopen(Request(url)).read()
    memoryFile = StringIO(remoteFile)
    pdfFile = PdfFileReader(memoryFile)
    """for pageNum in xrange(pdfFile.getNumPages()):
            currentPage = pdfFile.getPage(pageNum)
            writer.addPage(currentPage)
    outputStream = open("020601001000011.pdf","wb")
    writer.write(outputStream)
    outputStream.close()"""
    filtroDepa = Departamento.objects.values('ccdd','departamento').annotate(data=Count('ccdd'))
    data = list(filtroDepa)
    #zipear()
    return HttpResponse(json.dumps(data), content_type='application/json')


def zipear():
    url = 'http://192.168.221.123/desarrollo/'
    filenames_url = ['020601001000011.pdf','020601001000011.pdf']
    for file_url in filenames_url:
        z = zipfile.ZipFile('chau.zip',"w")
        z.write(file_url)    

