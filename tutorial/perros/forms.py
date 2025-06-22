from django import forms
from .models import UsuarioAdoptante

class UsuarioAdoptanteForm(forms.ModelForm):
    class Meta:
        model = UsuarioAdoptante
        fields = ['nombre', 'dni', 'email', 'raza_preferida', 'edad_preferida', 'tamaño_preferido']
        widgets = {
            'tamaño_preferido': forms.Select(choices=UsuarioAdoptante._meta.get_field('tamaño_preferido').choices)
        }