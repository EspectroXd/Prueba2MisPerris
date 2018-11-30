from django.shortcuts import render, redirect
from .models import FormularioAdopcion, FormularioRescatado
from django.contrib.auth.decorators import login_required
from . import forms

@login_required(login_url="/cuentas/login/")
def Formulario_adopcion_Listar(request):
    FormAdopAll = FormularioAdopcion.objects.all().order_by('nombre')
    return render(request,'adopcion/Formulario_adopcion_listar.html', {'FormAdopAll':FormAdopAll})

@login_required(login_url="/cuentas/login/")
def Formulario_rescatados_Listar(request):
    FormResAll = FormularioRescatado.objects.all().order_by('nombre')
    #FormResAll = FormularioRescatado.filter(nombre=request.nombre)
    return render(request,'adopcion/Rescate_listar.html', {'FormResAll':FormResAll})

@login_required(login_url="/cuentas/login/")
def Formulario_adopcion_Crear(request):
    if request.method=='POST':
        form=forms.CrearAdopcion(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.autor = request.user
            #intance.FormularioAdopcion.nombre=request.nombre; iguala la variable bd a la variable html
            instance.save()
            return redirect('Home')


    else:
        form = forms.CrearAdopcion()
    
    return render(request,'adopcion/adopcion_crear.html',{'form':form})

