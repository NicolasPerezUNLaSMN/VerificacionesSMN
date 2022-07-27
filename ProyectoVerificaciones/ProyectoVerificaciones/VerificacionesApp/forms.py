from django import forms
from VerificacionesApp.models import *

class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='AGREGAR IMAGEN: ')    

    
    class Meta:
        model = Imagen
        fields = ('image', )