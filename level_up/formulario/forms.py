from django import forms
from django.forms import ModelForm

from .models import Formul, Formul2


class StudentForm(ModelForm):
    GENEROS_SEXO=(
    ("Masculino", "Masculino"),
    ("Femenino", "Femenino"),
    )
    POESIA_CHOICES =(
    ("Lirica", "Lirica"),
    ("Epica", "Epica"),
    ("Dramatica", "Dramatica"),
    )
    genero= forms.ChoiceField(choices = GENEROS_SEXO)
    poesia= forms.ChoiceField(choices = POESIA_CHOICES)
    
    class Meta:
        model = Formul2
        
        fields = ('carne', 'name', 'direccion', 'genero', 
                  'tel','born','carrera','poesia')

        widgets = {
            'carne': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese carne valido'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Direccion'}),
            'tel': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefono (solo numeros)'}),
            'born': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Fecha de nacimiento'}),
            'carrera': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Carrera'}),
            
            

        }