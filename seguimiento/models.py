from __future__ import unicode_literals

from django.db import models

# Create your models here.

class vintage(models.Model):
    trimestre_form = models.CharField(max_length=10, default=0)
    ano_mes_form = models.CharField(max_length=10, default=0)
    ano_form = models.CharField(max_length=10)
    campana = models.CharField(max_length=20)
    flg_uso = models.IntegerField(default=0)
    producto = models.CharField(max_length=25)
    mora3_30d = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    mora6_60d = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    mora12 = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    ctas_uso = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    cuenta = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    segmento_riesgo = models.CharField(max_length=20)
    importe = models.DecimalField(max_digits=12, decimal_places=8, default=0)
    flg_convenio = models.IntegerField(default=0)
    linea_paralela = models.IntegerField(default=0)
    canal = models.IntegerField(default=0)
    flg_cierre = models.IntegerField(default=0)
    uso = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    uso_3m = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    uso_6m = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    uso_12m = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    linea_tdc = models.DecimalField(max_digits=12, decimal_places=8, default=0)
    ctas_linea_paralela = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    mora6_30d = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    def __str__(self):
        return self.ano_mes_form+' '+self.segmento_riesgo+' '+self.producto
