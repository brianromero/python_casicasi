from __future__ import unicode_literals
from django.db import models


#Clases validadas
class Departamento(models.Model):
    ccdd = models.CharField(db_column='CCDD',max_length=2, primary_key=True)
    departamento = models.CharField(db_column='DEPARTAMENTO', blank=True, null=True,max_length=50)
    fec_carga = models.DateTimeField(db_column='FEC_CARGA', blank=True, null=True)
    def __unicode__(self):
        return '%s , %s' % (self.ccdd, self.departamento)

    class Meta:
        managed = False
        db_table = 'TB_DEPARTAMENTO'


class Provincia(models.Model):
    ccdd = models.ForeignKey(Departamento, db_column='CCDD')
    ccpp = models.CharField(db_column='CCPP', max_length=2, primary_key=True)
    cod_prov = models.CharField(db_column='COD_PROV', max_length=4, blank=True, null=True)
    provincia = models.CharField(db_column='PROVINCIA', max_length=50, blank=True, null=True)
    fec_carga = models.DateTimeField(db_column='FEC_CARGA', blank=True, null=True)
   
    def __unicode__(self):
        return '%s , %s' % (self.ccpp, self.provincia)

    class Meta:
        managed = False
        db_table = 'TB_PROVINCIA'
        unique_together = (('ccdd', 'ccpp'))


class Distrito(models.Model):
    ubigeo = models.CharField(db_column='UBIGEO', max_length=6, primary_key=True)
    ccdd = models.ForeignKey(Departamento, db_column='CCDD')
    ccpp = models.ForeignKey(Provincia, db_column='CCPP')
    ccdi = models.CharField(db_column='CCDI', max_length=2, primary_key=True)
    distrito = models.CharField(db_column='DISTRITO', max_length=50, blank=True, null=True)
    region = models.CharField(db_column='REGION', max_length=50, blank=True, null=True)
    region_nat = models.CharField(db_column='REGION_NAT', max_length=50, blank=True, null=True)
    nro_aer = models.CharField(db_column='NRO_AER', max_length=50, blank=True, null=True)
    fec_carga = models.DateTimeField(db_column='FEC_CARGA', blank=True, null=True)
    
    def __unicode__(self):
        return '%s , %s' % (self.ccdd, self.departamento)

    class Meta:
        managed = False
        db_table = 'TB_DISTRITO'
        unique_together = (('ubigeo', 'ccdd', 'ccpp', 'ccdi'))


class Zona(models.Model):
    ubigeo = models.ForeignKey(Distrito, db_column='UBIGEO')
    zona = models.CharField(db_column='ZONA', max_length=10, primary_key=True) #blank=True, null=True)
    idmanzana = models.CharField(db_column='IDMANZANA', max_length=20, blank=True, null=True)
    aeu = models.IntegerField(db_column='AEU', blank=True, null=True)
    viv_aeu = models.IntegerField(db_column='VIV_AEU', blank=True, null=True)

    def __unicode__(self):
        return '%s , %s' % (self.ubigeo, self.zona)

    class Meta:
        managed = False
        db_table = 'TB_ZONA_CENSAL'

class TablaAeu(models.Model):
    object_id = models.IntegerField(db_column='OBJECT_ID', primary_key=True) 
    ubigeo = models.CharField(db_column='UBIGEO', max_length=6, blank=True, null=True)
    codccpp = models.CharField(db_column='CODCCPP', max_length=4, blank=True, null=True)
    zona = models.CharField(db_column='ZONA', max_length=5, blank=True, null=True)
    aeu_final = models.IntegerField(db_column='AEU_FINAL', blank=True, null=True)
    cant_viv = models.IntegerField(db_column='CANT_VIV', blank=True, null=True)
    seccion = models.IntegerField(db_column='SECCION',blank=True, null=True)
    llave_sec = models.CharField(db_column='LLAVE_SECC', max_length=50, blank=True, null=True)
    llave_aeu = models.CharField(db_column='LLAVE_AEU', max_length=50, blank=True, null=True)
    llave_ccpp = models.CharField(db_column='LLAVE_CCPP', max_length=50, blank=True, null=True)
    est_croquis = models.CharField(db_column='EST_CROQUIS', max_length=1, blank=True, null=True)
    est_seg = models.CharField(db_column='EST_SEG', max_length=1, blank=True, null=True)
    est_legajos = models.CharField(db_column='EST_LEGAJOS', max_length=1, blank=True, null=True)
    
    zona = models.CharField(db_column='ZONA', max_length=10, primary_key=True) #blank=True, null=True)
    idmanzana = models.CharField(db_column='IDMANZANA', max_length=20, blank=True, null=True)
    aeu = models.IntegerField(db_column='AEU', blank=True, null=True)
    viv_aeu = models.IntegerField(db_column='VIV_AEU', blank=True, null=True)

    def __unicode__(self):
        return '%s' % (self.ubigeo)

    class Meta:
        managed = False
        db_table = 'SEGM_ESP_AEU'
    