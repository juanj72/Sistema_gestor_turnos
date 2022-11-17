from django.urls import path
from .import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = [
    path('',views.inicio,name="inicio"),
    path('registro',views.registro,name="registro"),
    path('turno/<int:id>',views.turno,name='turno'),
    
    path('log',views.sesion,name="log"),
    path('turno_registro/<str:prueba>',views.turno_regis,name="registro_turno"),
    path('estado/<int:id>',views.estado,name='estado')
]

urlpatterns += staticfiles_urlpatterns()