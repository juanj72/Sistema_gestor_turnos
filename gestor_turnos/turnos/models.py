from django.db import models

class Personal (models.Model):
    nombre = models.CharField(max_length=100,null=False,blank=False)
    estado_per = models.IntegerField(max_length=5,null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

class Caja (models.Model):
    numcaja = models.IntegerField(max_length=25,null=False,blank=False)
    id_personal_per= models.ForeignKey(Personal,on_delete=models.CASCADE)
    tipocaja = models.IntegerField(max_length=5,null=False,blank=False)
    hora_res = models.TimeField(null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

class Turno (models.Model):
    id_caja_ca= models.ForeignKey(Caja,on_delete=models.CASCADE)
    numturno = models.IntegerField(max_length=25,null=False,blank=False)
    hora_solicitud = models.TimeField(null=False,blank=False)
    estado_tur = models.IntegerField(max_length=5,null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

class User (models.Model):
    id_turno_tur = models.ForeignKey(Turno,on_delete=models.CASCADE)
    cedula = models.IntegerField(max_length=25,null=False,blank=False) 
    correo = models.CharField(max_length=50,null=False,blank=False)
    telefono = models.CharField(max_length=10,null=False,blank=False)
    prioritario = models.IntegerField(max_length=5,null=False,blank=False)
    tipo_atencion = models.IntegerField(max_length=5,null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


