from dataclasses import fields
from pyexpat import model
from django import forms

from turnos.models import *


class formulariouser(forms.ModelForm):
    class Meta:
        model= User
        fields='__all__'




class formularioturno(forms.ModelForm):
    class Meta:
        model=Turno
        fields='__all__'