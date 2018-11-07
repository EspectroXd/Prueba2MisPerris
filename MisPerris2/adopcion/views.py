from django.shortcuts import render
from .models import FormularioAdopcion

def Formulario_adopcion_Listar(request):
    FormAdopAll = FormularioAdopcion.objects.all().order_by('nombre')
    return render(request,'adopcion/Formulario_adopcion_listar.html', {'FormAdopAll':FormAdopAll})
