from dataclasses import fields
from pyexpat import model
from django import forms


from turnos.models import *





class formulariouser(forms.ModelForm):
    correo = forms.EmailField()
    cedula=forms.IntegerField()
    telefono=forms.IntegerField()
    
    class Meta:
        model= User
        fields='__all__'

    # def clean_correo(self):
    #      correo=self.cleaned_data.get('correo')
    #     if User.objects.filter(correo=correo).exists:
    #         raise forms.ValidationError(u'ya existe un usuario con este correo!')

    #      if '.com' not in correo :
    #         raise forms.ValidationError(u'no tiene dominio (.com,.co,.edu ETC..)')

    #     if User.objects.filter(correo=correo):
    #         raise forms.ValidationError(u'correo ya existe')
        
    #     # if 'ñ' | 'Ñ' in correo:
    #     #     raise forms.ValidationError(u'no pueden haber EÑES tigre')

    #      return correo
    
    

    # def clean_cedula(self):
    #     cedula=self.cleaned_data.get('cedula')
    
    #     if cedula >= 1:
    #         #print('hola')
    #         if  len(str(cedula))<=4 or len(str(cedula))>10:
    #             print('hola')
    #             raise forms.ValidationError(u'el numero debe tener minimo 4 caracteres y maximo 10')
                
            
    #     else:
    #         raise forms.ValidationError(u'el numero digitado no puede ser negativo.')
            

    

      




class formularioturno(forms.ModelForm):
    

    class Meta:
        model=Turno
        fields=['id_user_tur','tipo_turno']