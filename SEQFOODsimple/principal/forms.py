from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _




class Busqueda(forms.Form):
	texto_busqueda=forms.CharField(help_text="Introduce el codigo o palabras clave a buscar")

