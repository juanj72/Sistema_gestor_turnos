from email import message
from django.shortcuts import render,redirect
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
          return redirect('registro_turno')
          successs=True

          
              
     return render(request,"registro.html",{"formulario":formulario,"successs":successs,"turno":formulario_turno})

    except:
        messa=True
        


        return render(request,"registro.html",{"formulario":formulario,"error":messa})


def turno_regis(request):
    turno=formularioturno(request.POST or None)
    nomb=None
    mensa=None
    formu_val=True

    
    if request.method=='POST':
        if turno.is_valid():
            nomb=request.POST['id_user_tur']
            
            turno.save()
            formu_val=False
            mensa=True

    return render (request,"turno.html",{"turno":turno,"mensaje":mensa,"usuario":nomb,"validador":formu_val})


      
    

    
def turno(request,id):

    tur=Turno.objects.filter(id_user_tur=id)


    return render(request,"user.html",{"turno":tur})

def tetris(request):
    return render(request,"tetris.html")

def sesion(request):
    return render(request,"userlog.html")

def memoria(request):
    return render(request,"memoria.html")