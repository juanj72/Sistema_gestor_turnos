from django import forms

from turnos.models import *


class Formulariopersonal(forms.ModelForm):
    class Meta:
        model = Personal
        fields='__all__'