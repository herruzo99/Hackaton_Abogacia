# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


from django.db import models



class Comentario(models.Model):
    idArticulo = models.IntegerField(default=0)
    idComentario = models.IntegerField(default=0)
    idComentarioPadre = models.IntegerField(default=0)
    cita = models.CharField(max_length=5000)
    texto = models.CharField(max_length=5000)
    votos = models.IntegerField(default=0)


class Articulo(models.Model):
    tipo = models.IntegerField(default=1) #1 = oficial 2 = sugerencia 2 = aceptado 3 = rechazado
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=500)
    articulo = models.CharField(max_length=5000)
    votos = models.IntegerField(default=0)
    idArticulo = models.IntegerField(default=0)


