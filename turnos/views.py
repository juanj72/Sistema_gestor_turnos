from email import message
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from turnos.forms import *
from django.db import connection

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
    

    # if request.method=='POST':
    #    if request.POST.get('tipo_turno'):
    #     print("hola")
    #     print("\n",request.POST['tipo_turno'])
    #     turno=Turno(
    #         id_user_tur=datos_usuario,
    #         tipo_turno=request.POST['tipo_turno']

    #     )
    #     turno.save()
    #     return redirect('turno',datos_usuario.id)
        
    

   
    
    return render (request,"turno.html",{"obj":datos_usuario})


def reclamo(request,correo):
    datos_usuario=User.objects.get(correo=correo)
    turnos=Turno(
        id_user_tur=datos_usuario,
        tipo_turno=2


    )
    #print("hola desde turnos")
    turnos.save()
    return redirect('turno',datos_usuario.id)


    
    
def venta(request,correo):
    datos_usuario=User.objects.get(correo=correo)

    turnos=Turno(
        id_user_tur=datos_usuario,
        tipo_turno=1


    )
    print("hola desde turnos")
    turnos.save()
    return redirect('turno',datos_usuario.id)



def asesoria(request,correo):
    datos_usuario=User.objects.get(correo=correo)

    turnos=Turno(
        id_user_tur=datos_usuario,
        tipo_turno=3


    )
    print("hola desde turnos")
    turnos.save()
    return redirect('turno',datos_usuario.id)


    

    
def turno(request,id):

    tur=Turno.objects.filter(id_user_tur=id)
    turnos=Turno.objects.all()
    print(tur.get().id)
    turno_id=tur.get().id


    return render(request,"user.html",{"turno":tur,"turno_id":turno_id,"turnos":turnos})


def estado(request,id):
    tur=Turno.objects.filter(id=id)
    numero=tur.get().id

    return render(request,"estado.html",{"turno":tur})

def ver_turnos():

    with connection.cursor() as cursor:  # Activamos un cursor para las consultas a la BD
    


        # Ejecutar una linea SQL En este caso llamamos un procedimiento almacenado
        cursor.execute('call ver_turnos()')
        #total=total_fecha(fecha)

        columns = []  # Para guardar el nombre de las columnas

        # Recorrer la descripcion (Nombre de la columna)
        for column in cursor.description:

            columns.append(column[0])  # Guardando el nombre de las columnas

        data = []  # Lista con los datos que vamos a enviar en JSON

        for row in cursor.fetchall():  # Recorremos las fila guardados de la BD

            # Insertamos en data un diccionario
            data.append(dict(zip(columns, row)))

        cursor.close()  # Se cierra el cursor para que se ejecute el procedimiento almacenado

        connection.commit()  # Enviamos la sentencia a la BD
        connection.close()

        return data


def ventana_monitor(request):
    datos_turnos=ver_turnos()

    return render(request,'monitor.html',{"turnos_ventana":datos_turnos})






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