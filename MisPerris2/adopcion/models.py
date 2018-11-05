from django.db import models

class FormularioAdopcion(models.Model):
    rut = models.CharField(max_length=12, help_text="Ej: 12.123.123-1" , unique=True)
    correo = models.CharField(max_length=100)
    nombre = models.CharField(max_length=60, help_text="Nombre Completo")
    fechaNac = models.DateTimeField(default=timezone.now)
    region = models.CharField(max_length=60, help_text="region")
    ciudad = models.CharField(max_length=60, help_text="ciudad")
    tipoVivienda = models.CharField(max_length=60, help_text="vivienda")
