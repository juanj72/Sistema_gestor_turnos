from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def inicio(request):
    return render(request,"index.html")

def registro(request):
    return render(request,"registro.html")

def turno(request):
    return render(request,"user.html")

def tetris(request):
    return render(request,"tetris.html")