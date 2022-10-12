from django.urls import path
from .import views



urlpatterns = [
    path('',views.inicio,name="inicio"),
    path('registro',views.registro,name="registro"),
    path('turno',views.turno,name='turno'),
    
    path('log',views.sesion,name="log")
]