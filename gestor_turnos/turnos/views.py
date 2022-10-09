from email import message
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def inicio(request):
    return render(request,"index.html")

def registro(request):
    form=UserCreationForm(request.POST)
    if request.method=='POST':
       
        if form.is_valid():
            username=form.cleaned_data['username']
            message.success(request,f'Usuario {username} creado')
        else:
            form=UserCreationForm()
        


    return render(request,"registro.html",{"form":form})

def turno(request):
    return render(request,"user.html")

def tetris(request):
    return render(request,"tetris.html")

def sesion(request):
    return render(request,"userlog.html")