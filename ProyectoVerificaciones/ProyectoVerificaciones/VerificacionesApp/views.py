from django.shortcuts import render

from django.forms import modelformset_factory
from .models import Evento, Imagen
from .forms import ImageForm, EventoFormulario

from ProyectoVerificaciones.settings import MAPBOX_ACCESS_TOKEN

# Create your views here.


def inicio(request):



    return render(request, "VerificacionesApp/index.html")



def nuevoEvento(request):

   
    

    ImageFormSet = modelformset_factory(Imagen, form=ImageForm, extra=10, min_num= 1, )
    
    mensajeError = 'Completar los campos marcados con * y enviar una foto como mínimo'

  
    #Si ingreso con metodo post
    if request.method == "POST":

      formset = ImageFormSet(request.POST, request.FILES, queryset=Imagen.objects.none())
      miFormulario = EventoFormulario(request.POST)
      
      
      #Si el formulario se lleno bien
      if formset.is_valid() and miFormulario.is_valid():
          
          i = miFormulario.cleaned_data
          
          evento = Evento(descripcion=i["descripcion"],
                          linkDireccion=i["linkDireccion"],
                          localidadAfectada=i["localidadAfectada"],
                          tipoEvento=i["tipoEvento"],
                          fechaDelEvento=i["fechaDelEvento"],
                          nombreFuente=i["nombreFuente"],
                          color=i["color"],
                          tipo=i["tipo"],
                          areaPimetAfectada=i["areaPimetAfectada"],
                          lat=i["lat"],
                          long=i["long"])

          

          evento.save()
          
          #imagen
          for form in formset.cleaned_data:
                  
                    if form:
                        img = form['image']
                        imagen = Imagen()
                        imagen.evento= evento
                        imagen.image = img
                        imagen.save()
          
          
          
          return inicio(request)
          
      else:  #si el formulario no se lleno bien

          mensajeError = '¡¡¡ El formulario no ha sido válido, verifique enviar una imagen como mínimo... !!!'
    
    
      

    formset = ImageFormSet(queryset=Imagen.objects.none())
    miFormulario = EventoFormulario()
    
    return render(request, "VerificacionesApp/nuevoEvento.html",  {'formset': formset, "miFormulario":miFormulario,'mensajeError':mensajeError, "MAPBOX_ACCESS_TOKEN":MAPBOX_ACCESS_TOKEN})