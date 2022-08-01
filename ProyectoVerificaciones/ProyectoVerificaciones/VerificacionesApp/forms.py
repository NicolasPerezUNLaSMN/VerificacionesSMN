from django import forms
from VerificacionesApp.models import *
import datetime


class EventoFormulario(forms.Form):
    

    #Sobre el evento
    descripcion = forms.CharField(max_length=400)
    linkDireccion = forms.CharField(max_length=200)
    localidadAfectada  = forms.CharField(max_length=200)
    tipoEvento = forms.CharField(max_length=200)
    fechaDelEvento =  forms.DateField(initial=datetime.date.today)
    
    #Sobre la fuente
    nombreFuente  =forms.CharField(max_length=200)
    
    #Sobre alertas
    color= forms.CharField(max_length=200)
    tipo= forms.CharField(max_length=200)
    
    #Geografico
    areaPimetAfectada = forms.CharField(max_length=200)
    lat = forms.FloatField()
    long = forms.FloatField()



class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='AGREGAR IMAGEN: ')    

    
    class Meta:
        model = Imagen
        fields = ('image', )