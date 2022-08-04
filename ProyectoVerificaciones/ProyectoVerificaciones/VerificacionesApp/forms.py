from django import forms
from VerificacionesApp.models import *
from .constantes import CHOICES_PIMET


class EventoFormulario(forms.Form):
    
    CHOICES_EVENTO = (("Lluvias/Inundaciones", "Lluvias/Inundaciones"),("Granizo", "Granizo"),("Nieve acumulada", "Nieve acumulada"), ("Viento", "Viento"),("Zonda", "Zonda"),)
    CHOICES_COLOR = (("Rojo", "Rojo"),("Naranja", "Naranja"), ("Amarillo", "Amarillo"), ("Verde/Sin Alerta", "Verde/Sin Alerta"), ("Advertencia", "Advertencia"),)
    CHOICES_TIPO = (("Sin Alerta", "Sin Alerta"), ("Lluvias fuertes", "Lluvias fuertes"), ("Tormentas fuertes", "Tormentas fuertes"), ("Nevadas fuertes", "Nevadas fuertes"), ("Vientos", "Vientos"),("Zonda","Zonda"), ("Advertencia visibilidad","Advertencia visibilidad"),)
    
    
    
    #Sobre el evento
    descripcion =  forms.CharField(widget=forms.Textarea(attrs={"class":"form-control"}))
    linkDireccion =  forms.CharField(required=False,widget=forms.TextInput(attrs={"class":"form-control"}))
    localidadAfectada  =  forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    tipoEvento = forms.ChoiceField(widget=forms.Select(attrs={"class":"form-control"}), choices=CHOICES_EVENTO)
    fechaDelEvento =  forms.DateTimeField(widget=forms.widgets.DateInput(attrs={'type': 'date',"class":"form-control"}))
    
    #Sobre la fuente
    nombreFuente  =  forms.CharField(required=False,widget=forms.TextInput(attrs={"class":"form-control"}))
    
    #Sobre alertas
    color= forms.ChoiceField(widget=forms.Select(attrs={"class":"form-control"}), choices=CHOICES_COLOR)
    tipo= forms.ChoiceField(widget=forms.Select(attrs={"class":"form-control"}), choices=CHOICES_TIPO)
    
    #Geografico
    areaPimetAfectada = forms.ChoiceField(required=False,widget=forms.Select(attrs={"class":"form-control"}), choices=CHOICES_PIMET)
    lat = forms.FloatField(label="Latitud", widget=forms.NumberInput(attrs={"class":"form-control"}))
    long = forms.FloatField(label="Longitud", widget=forms.NumberInput(attrs={"class":"form-control"}))



class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='AGREGAR IMAGEN: ',widget=forms.FileInput(attrs={"class":"form-control"})   ) 

    
    class Meta:
        model = Imagen
        fields = ('image', )