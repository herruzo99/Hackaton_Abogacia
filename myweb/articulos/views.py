# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from .models import Articulo,Comentario


def oficial(request):
    articulos = Articulo.objects.order_by('-votos').filter(tipo = 1)
    context = {'articulos': articulos}
    return render(request, 'articulos/index.html', context)

def sugerencia(request):
    articulos = Articulo.objects.order_by('-votos').filter(tipo = 2)
    context = {'articulos': articulos}
    return render(request, 'articulos/sugerencia.html', context)

def registro(request):
    articulos = Articulo.objects.order_by('-votos').filter(tipo__in = [3,4]  )
    context = {'articulos': articulos}
    return render(request, 'articulos/registro.html', context)

def articulo(request, articulo_id):
    articulo = Articulo.objects.order_by('-votos').filter(idArticulo = articulo_id)
    comentarios = Comentario.objects.order_by('-votos').filter(idArticulo = articulo_id)
    comentariosPadre = comentarios.filter(idComentarioPadre = 0)
    
    context = {'articulo': articulo, 'comentarios': comentarios, 'comentariosPadre': comentariosPadre}
    return render(request, 'articulos/articulo.html', context)