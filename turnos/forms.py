from dataclasses import fields
from pyexpat import model
from django import forms


from turnos.models import *


class formulariouser(forms.ModelForm):
    correo = forms.EmailField(label='Correo electrónico',widget=forms.TextInput(attrs={"placeholder":'ingrese un correo electrónico \'gmail\' o \'hotmail\''}))
    cedula = forms.IntegerField(label='Cédula',widget=forms.TextInput(attrs={"placeholder":'ingrese su número de documento'}))
    telefono = forms.IntegerField(label='Teléfono',widget=forms.TextInput(attrs={"placeholder":'ingrese su numero de teléfono'}))    

    class Meta:
        model = User
        fields = ('cedula','correo','telefono')
       
        

    def clean_correo(self):
        correo=self.cleaned_data['correo']
        if correo.split('@')[1] not in ['gmail.com','campusucc.edu.co']:
            raise forms.ValidationError('Ingrese un email válido por favor, (\"gmail.com\",\"campusucc.edu.co\")')
        return correo

  
            

      




class formularioturno(forms.ModelForm):
    

    class Meta:
        model=Turno
        fields=['id_user_tur','tipo_turno']