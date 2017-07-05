# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.



class Alimento(models.Model):
	c2dna=models.CharField(max_length=255, primary_key=True)
	origen=models.CharField(max_length=70)
	nombre=models.CharField(max_length=30)
	TIPO_CATEGORIA=(
		('Carne',"Carne"),
		('Pescado',"Pescado"),
		('Lacteo',"Lacteo"),
		('Fruta',"Fruta"),
		('Otra',"Otra")
		)
	categoria=models.CharField(max_length=10, choices=TIPO_CATEGORIA, default="Otra")

	def __unicode__(self):
		return self.nombre