# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from .models import Alimento
from .forms import Busqueda
from django.core.urlresolvers import reverse
from django.views import generic
from django.db.models import Count

from django.shortcuts import render

def index(request):
	num_alimentos=Alimento.objects.all().count()
	query_categorias=Alimento.objects.values("categoria").annotate(cuenta=Count("categoria"))
	
	return render(request, "principal/index.html", context={"num_alimentos": num_alimentos, "categorias":query_categorias})
	


def gestionBusqueda(request):
	if request.method == 'POST':
		texto=request.POST["busqueda"]
		#Cambiar esto cuando se sepa formato de c2dna
		query_result=Alimento.objects.filter(nombre__icontains=texto)
		if not query_result:
			query_result=Alimento.objects.filter(c2dna=texto)
		return render(request, "principal/resultadoBusqueda.html", context={"resultado":query_result})

	return render(request, "principal/resultadoBusqueda.html")


class VistaDetalleAlimento(generic.DetailView):
	model=Alimento
	template_name="principal/detalleAlimento.html"
	context_object_name="detalleAlimento"

def busquedaAvanzada(request):
	return render(request, "principal/busquedaAvanzada.html")