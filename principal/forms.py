# -*- coding: utf-8 -*-
from django import forms
from .models import *
from django.contrib.auth.hashers import *
from principal.models import Usuario


class UserForm(forms.ModelForm):



    usu_cedula=forms.CharField(label="Cedula",widget=forms.TextInput(attrs={'style':'width: 223px','class':'form-group'}))
    usu_nombre=forms.CharField(label="Nombres",widget=forms.TextInput(attrs={'style':'width: 223px','class':'form-group'}))
    usu_apellido=forms.CharField(label="Apellidos",widget=forms.TextInput(attrs={'style':'width: 223px','class':'form-group'}))
    usu_correo=forms.CharField(label="Correo",widget=forms.TextInput(attrs={'style':'width: 223px','class':'form-group'}))
    password=forms.CharField(label="Contraseña ",widget=forms.PasswordInput(attrs={'style':'width: 223px','class':'form-group'}))
    passwordAgain=forms.CharField(label="Confirmar Contraseña",widget=forms.PasswordInput(attrs={'style':'width: 223px','class':'form-group'}))


    class Meta:
        model= Usuario
        fields=('usu_cedula','usu_nombre','usu_apellido','usu_correo','password',)

        labels = {
            'usu_cedula': ('Cedula'),
        }


    def clean_password(self):
        password = self.cleaned_data['password']
        print()
        if  password<> "":
            return make_password(password)
        else:
            raise forms.ValidationError('Las contraseñas no son iguales')