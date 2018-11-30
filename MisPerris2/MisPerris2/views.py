from django.http import HttpResponse 
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def homepage(request):
    #return HttpResponse('homepage')
    return render(request,'homepage.html') 
    
@login_required(login_url="/cuentas/login/")
def Home(request):
    #return HttpResponse('Home')
    return render(request,'Home.html') 

def about (request):
    #return HttpResponse('about')
    return render(request,'about.html')

