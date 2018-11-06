from django.shortcuts import render
from .models import FormularioAdopcion
from django.views.generic.edit import CreateView
from django.urls import reverse

def Formulario_adopcion_Listar(request):
    FormAdopAll = FormularioAdopcion.objects.all().order_by('nombre')
    return render(request,'adopcion/Formulario_adopcion_listar.html', {'FormAdopAll':FormAdopAll})

def Formulario_adopcion_crear(CreateView):
    model = FormularioAdopcion
    success_url = reverse('adopcion:list')
    fields = ['rut', 'correo', 'nombre', 'fechaNac', 'region', 'ciudad', 'tipoVivienda']