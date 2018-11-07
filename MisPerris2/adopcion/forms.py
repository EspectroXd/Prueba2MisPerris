from django import forms
from . import models

class CrearAdopcion(forms.ModelForm):
    class Meta:
        model= models.FormularioAdopcion
        fields=['rut','correo','nombre','fechaNac','region','ciudad','tipoVivienda']

