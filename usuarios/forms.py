from django import forms
from django.forms import ModelForm, widgets
from django.utils.translation import gettext_lazy as _

from usuarios.models import  Usuario, Beneficiario, Acudiente, Padrino, Referencia


class UsuarioForm(ModelForm):
    nombres = forms.CharField(min_length=2, max_length=16)
    apellidos = forms.CharField(min_length=2, max_length=16)    
    class Meta:
        model= Usuario
        exclude=['estado','user']
        widgets={
            'fecha_nacimiento': widgets.DateInput(attrs={'type':'date'})
        }
        
class BeneficiarioForm(ModelForm):
    class Meta:
        model=Beneficiario
        exclude=['estado']
        widgets={
            'fechaNacimiento': widgets.DateInput(attrs={'type':'date'})
        }   

class AcudienteForm(ModelForm):
    class Meta:
        model=Acudiente
        exclude=['estado']

class PadrinoForm(ModelForm):
    class Meta:
        model=Padrino
        exclude=['estado']
        
class ReferenciaForm(ModelForm):
    class Meta:
        model=Referencia
        exclude=['estado']



