from random import choices
from django.db import models
from django.core.exceptions import ValidationError
import re


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
    (1,'Prioritario'),
    (0,'No prioritario')
]

tipo_turno=[
    (1,'Ventas'),
    (2,'Reclamos'),
    (3,'Asesoría')
]

estado_turno=[
    (1,'En espera'),
    (2,'Atención'),
    (3,'Atendido'),
]



    









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
    

    def validate_cedula(value):
        print(type(value))
        if len(str(value))<4 or len(str(value))>10:
             raise ValidationError(('%(value)s El número tiene que tener más de 4 digitos y menos de 10'),params={'value':value})
        
        if value<=0:
            print("hola")
            raise ValidationError(('%(value)s El número tiene que ser mayor a 0'),params={'value':value})

    
    def validador_telefono(value):
        if int(value)<=0:
            raise ValidationError('Por favor números mayores y diferentes a cero')
        if len(value)<10 or len(value)>10:
            raise ValidationError('El número de teléfono solo puede tener 10 dígitos')

        if 'e' in str(value) or 'E' in str(value):
            raise ValidationError('No se permiten caracteres alfabéticos')


    def validar_correo(value):
        regex=r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if(re.fullmatch(regex, value)):
            print("Valid Email")
 
        else:
            raise ('direccion de correo inválida')







    cedula = models.IntegerField(max_length=50,null=False,blank=False,unique=True,validators=[validate_cedula]) 
    correo = models.CharField(max_length=50,null=False,blank=False,unique=True,validators=[validar_correo])
    telefono = models.CharField(max_length=50,null=False,blank=False,validators=[validador_telefono],verbose_name='Teléfono')
    prioritario = models.IntegerField(max_length=5,null=True,blank=True,choices=prioritarios,default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.correo)

class Turno (models.Model):
    id_user_tur= models.ForeignKey(User,on_delete=models.CASCADE)
    numturno = models.CharField(max_length=25,null=False,blank=False)
    estado_tur = models.IntegerField(max_length=5,null=False,blank=False,default=1,choices=estado_turno)
    tipo_turno = models.IntegerField(max_length=5,null=False,blank=False,choices=tipo_turno)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        if self.estado_tur==1:
            return f'EN ESPERA numero: {str(self.id)}'
        if self.estado_tur==2:
            return f'En ventanilla: {str(self.id)}'
        if self.estado_tur==3:
            return f'Atendido: {self.id_user_tur} numero: {str(self.id)}'
        

    

class Caja (models.Model):
    numcaja = models.IntegerField(max_length=25,null=False,blank=False)
    id_personal_per= models.ForeignKey(Personal,on_delete=models.CASCADE)
    tipocaja = models.IntegerField(max_length=5,null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    id_turno_tur= models.ForeignKey(Turno,on_delete=models.CASCADE)



