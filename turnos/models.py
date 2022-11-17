from random import choices
from django.db import models
from django.core.exceptions import ValidationError


# class Personal (models.Model):
#     nombre = models.CharField(max_length=100,null=False,blank=False)
#     estado_per = models.IntegerField(max_length=5,null=False,blank=False)
#     created_at = models.DateTimeField(auto_now_add=True)
#     update_at = models.DateTimeField(auto_now=True)
#     def __str__(self):
#         return self.nombre

# class Caja (models.Model):
#     numcaja = models.IntegerField(max_length=25,null=False,blank=False)
#     id_personal_per= models.ForeignKey(Personal,on_delete=models.CASCADE)
#     tipocaja = models.IntegerField(max_length=5,null=False,blank=False)
#     hora_res = models.TimeField(null=False,blank=False)
#     created_at = models.DateTimeField(auto_now_add=True)
#     update_at = models.DateTimeField(auto_now=True)

#     # def __str__(self):
#     #     return self.id_personal_per

# class Turno (models.Model):
#     id_caja_ca= models.ForeignKey(Caja,on_delete=models.CASCADE)
#     numturno = models.IntegerField(max_length=25,null=False,blank=False)
#     hora_solicitud = models.TimeField(null=False,blank=False)
#     estado_tur = models.IntegerField(max_length=5,null=False,blank=False)
#     created_at = models.DateTimeField(auto_now_add=True)
#     update_at = models.DateTimeField(auto_now=True)
    

# class User (models.Model):
#     id_turno_tur = models.ForeignKey(Turno,on_delete=models.CASCADE)
#     cedula = models.IntegerField(max_length=25,null=False,blank=False) 
#     correo = models.CharField(max_length=50,null=False,blank=False)
#     telefono = models.CharField(max_length=10,null=False,blank=False)
#     prioritario = models.IntegerField(max_length=5,null=False,blank=False)
#     tipo_atencion = models.IntegerField(max_length=5,null=False,blank=False)
#     created_at = models.DateTimeField(auto_now_add=True)
#     update_at = models.DateTimeField(auto_now=True)


prioritarios=[
    (1,'prioritario'),
    (0,'No prioritario')
]

tipo_turno=[
    (1,'ventas'),
    (2,'reclamos'),
    (3,'asesoría')
]

estado_turno=[
    (1,'en espera'),
    (2,'atencion'),
    (3,'atendido'),
]



    


def validador_cedula(value):
    if len(value)<4 | len(value)>10:
        raise ValidationError('el dato ingresado tiene que estar en un rago de 4 a 10 caracteres')
    if int(value)<=0 :
        raise ValidationError('ingrese un criterio valido, mayor que cero')





class Personal (models.Model):
    nombre = models.CharField(max_length=100,null=False,blank=False)
    estado_per = models.IntegerField(max_length=5,null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class User (models.Model):

    # def validate_numero(value):
    #  if len(str(value))<10 | len(value)>10:
    #      raise ValidationError(('%(value)s solo puede tener al menos 10 caracteres'),params={'value':value})
        
    #  if value<0:
    #      raise ValidationError(('%(value)s el numero tiene que ser mayor a 0'),params={'value':value})
    

    # def validate_cedula(value):
    #     if len(value)<4 | len(value)>10:
    #          raise ValidationError(('%(value)s el numero tiene que tener mas de 4 digitos y menos de 10'),params={'value':value})
        
    #     if int(value)<=0:
    #         raise ValidationError(('%(value)s el numero tiene que ser mayor a 0'),params={'value':value})






    cedula = models.IntegerField(max_length=50,null=False,blank=False,unique=True) 
    correo = models.CharField(max_length=50,null=False,blank=False,unique=True)
    telefono = models.CharField(max_length=50,null=False,blank=False)
    prioritario = models.IntegerField(max_length=5,null=False,blank=False,choices=prioritarios)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.correo

class Turno (models.Model):
    id_user_tur= models.ForeignKey(User,on_delete=models.CASCADE)
    numturno = models.CharField(max_length=25,null=False,blank=False)
    estado_tur = models.IntegerField(max_length=5,null=False,blank=False,default=1,choices=estado_turno)
    tipo_turno = models.IntegerField(max_length=5,null=False,blank=False,choices=tipo_turno)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    

    

class Caja (models.Model):
    numcaja = models.IntegerField(max_length=25,null=False,blank=False)
    id_personal_per= models.ForeignKey(Personal,on_delete=models.CASCADE)
    tipocaja = models.IntegerField(max_length=5,null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    id_turno_tur= models.ForeignKey(Turno,on_delete=models.CASCADE)



