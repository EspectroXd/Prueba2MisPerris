from django.db import models
from django.utils import timezone

class FormularioAdopcion(models.Model):
    REGION_CHOICES = (
        ('Tarapaca','Tarapaca'),
        ('Antofagasta','Antofagasta'),
        ('Atacama','Atacama'),
        ('Coquimbo','Coquimbo'),
        ('Valparaiso','Valparaiso'),
        ('O´Higgins','O´Higgins'),
        ('Maule','Maule'),
        ('Concepcion','Concepcion'),
        ('Araucania','Araucania'),
        ('Los Lagos','Los Lagos'),
        ('Aysén','Aysén'),
        ('Magallanes','Magallanes'),
        ('Metropolitana','Metropolitana'),
        ('Los Rios','Los Rios'),
        ('Arica','Arica'),
        ('Ñuble','Ñuble'),
    )
    CIUDAD_CHOICES = (
        ('Iquique','Iquique'),
        ('Antofagasta','Antofagasta'),
        ('Copiapo','Copiapo'),
        ('Coquimbo','Coquimbo'),
        ('Valparaiso','Valparaiso'),
        ('Rancagua','Rancagua'),
        ('Talca','Talca'),
        ('Concepcion','Concepcion'),
        ('Temuco','Temuco'),
        ('Puerto Montt','Puerto Montt'),
        ('Coyhiaique','Coyhiaique'),
        ('Punta Arenas','Punta Arenas'),
        ('Santiago','Santiago'),
        ('Valdivia','Valdivia'),
        ('Arica','Arica'),
        ('Chillán','Chillán'),
    )

    VIVIENDA_CHOICES = (
        ('Casa patio grande','Casa patio grande'),
        ('Casa patio pequeño','Casa patio pequeño'),
        ('Casa sin patio','Casa sin patio'),
        ('Departamento','Departamento'),
    )

    rut = models.CharField(max_length=12, help_text="Ej: 12.123.123-1" , unique=True)
    correo = models.CharField(max_length=100)
    nombre = models.CharField(max_length=60, help_text="Nombre Completo")
    fechaNac = models.DateTimeField(default=timezone.now)
    region = models.CharField(max_length=60, choices = REGION_CHOICES ,help_text="region")
    ciudad = models.CharField(max_length=60, choices = CIUDAD_CHOICES , help_text="ciudad")
    tipoVivienda = models.CharField(max_length=60, choices = VIVIENDA_CHOICES , help_text="vivienda")

    def __str__(self):
        return self.rut