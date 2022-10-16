from email import message
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from turnos.forms import *


# Create your views here.

def inicio(request):

    return render(request,"index.html")

def registro(request):
    formulario=Formulariopersonal
    

    return render(request,"registro.html",{"formulario":formulario})

def turno(request):
    return render(request,"user.html")

def tetris(request):
    return render(request,"tetris.html")

def sesion(request):
    return render(request,"userlog.html")