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
    prueba_pal='hola'
    try:
     formulario_turno=formularioturno()
     formulario=formulariouser(request.POST or None)
     
     if request.method=='POST':
        print(request.POST['cedula'])
        if formulario.is_valid:
        
          formulario.save()
          prueba_pal=request.POST['correo']
          print(request.POST['cedula'])
          return redirect('registro_turno',prueba_pal)
          successs=True

          
              
     return render(request,"registro.html",{"formulario":formulario,"successs":successs,"turno":formulario_turno})

    except:
        messa=True
      
        


        return render(request,"registro.html",{"formulario":formulario,"error":messa})




def turno_regis(request,prueba):

    datos_usuario=User.objects.get(correo=prueba)
    

    if request.method=='POST':
       if request.POST.get('tipo_turno'):
        print("hola")
        print("\n",request.POST['tipo_turno'])
        turno=Turno(
            id_user_tur=datos_usuario,
            tipo_turno=request.POST['tipo_turno']

        )
        turno.save()
        return redirect('turno',datos_usuario.id)
        
    

   
    
    return render (request,"turno.html",{"obj":datos_usuario})


      
    

    
def turno(request,id):

    tur=Turno.objects.filter(id_user_tur=id)
    print(tur.get().id)
    turno_id=tur.get().id


    return render(request,"user.html",{"turno":tur,"turno_id":turno_id})


def estado(request,id):
    tur=Turno.objects.filter(id=id)
    numero=tur.get().id

    return render(request,"estado.html",{"turno":tur})



def tetris(request,id):
    tur=Turno.objects.filter(id=id)
    numero=tur.get().id

    return render(request,"tetris.html",{"turno":tur,"id_tur":numero})

def sesion(request):
    return render(request,"userlog.html")




def memoria(request,id):
    tur=Turno.objects.filter(id=id)
    numero=tur.get().id
    return render(request,"memoria.html",{"turno":tur,"id_tur":numero})