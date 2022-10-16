from email import message
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from turnos.forms import *


# Create your views here.

def inicio(request):

    return render(request,"index.html")

def registro(request):
    messa=None
    successs=None
    try:
     formulario_turno=formularioturno()
     formulario=formulariouser(request.POST or None)
     
     if request.method=='POST':
        if formulario.is_valid:
        
          formulario.save()
          successs=True
          
              
     return render(request,"registro.html",{"formulario":formulario,"successs":successs,"turno":formulario_turno})

    except:
        messa=True
        


        return render(request,"registro.html",{"formulario":formulario,"error":messa})


def turno_regis(request):
    turno=formularioturno()
    return render (request,"turno.html",{"turno":turno})


      
    

    
def turno(request):
    return render(request,"user.html")

def tetris(request):
    return render(request,"tetris.html")

def sesion(request):
    return render(request,"userlog.html")