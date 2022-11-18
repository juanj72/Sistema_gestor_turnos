from dataclasses import fields
from pyexpat import model
from django import forms


from turnos.models import *


class formulariouser(forms.ModelForm):
    correo = forms.EmailField()
    cedula = forms.IntegerField()
    telefono = forms.IntegerField()

    class Meta:
        model = User
        fields = '__all__'

    def clean_correo(self):
        correo=self.cleaned_data['correo']
        if correo.split('@')[1] not in ['gmail.com','hotmail.com']:
            raise forms.ValidationError('ingrese un email valido, por favor, (\"gmail.com\",\"campusucc.edu.co\")')
        return correo

  
            

      




class formularioturno(forms.ModelForm):
    

    class Meta:
        model=Turno
        fields=['id_user_tur','tipo_turno']