from django import forms
from django.forms import widgets
from .models import Usuario

class UsuarioForm(forms.ModelForm):

    class Meta:
      model = Usuario

      fields = [
          'nombre',
          'apellido',
          'direccion',
          'telefono',
          'correo',
          'clave',
      ]
      labels = {
          'nombre':'Nombre',
          'apellido':'Apellido',
          'direccion':'Direccion',
          'telefono':'Teléfono',
          'correo':'Correo',
          'clave':'Contraseña',
      }
      widgets = {
          'nombre':forms.TextInput(attrs={'class':'form-control', 'requered':''}),
          'apellido':forms.TextInput(attrs={'class':'form-control','required':''}),
          'direccion':forms.TextInput(attrs={'class':'form-control','required':''}),
          'telefono':forms.NumberInput(attrs={'class':'form-control','required':''}),
          'correo':forms.EmailInput(attrs={'class':'form-control','required':''}),
          'clave':forms.PasswordInput(attrs={'class':'form-control','required':''}),
      }

