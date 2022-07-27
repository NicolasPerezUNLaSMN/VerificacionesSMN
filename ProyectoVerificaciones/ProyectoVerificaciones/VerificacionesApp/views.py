from django.shortcuts import render

from django.forms import modelformset_factory
from .models import Evento, Imagen
from .forms import ImageForm

# Create your views here.


def inicio(request):



    return render(request, "VerificacionesApp/index.html")



def nuevoEvento(request):

   
    

    ImageFormSet = modelformset_factory(Imagen, form=ImageForm, extra=10, min_num= 1, )
    
    mensajeError = 'Completar los campos marcados con * y enviar una foto como mínimo'

  
    #Si ingreso con metodo post
    if request.method == "POST":

      formset = ImageFormSet(request.POST, request.FILES, queryset=Imagen.objects.none())

      
      
      #Si el formulario se lleno bien
      if formset.is_valid():
          
    
          evento = Evento()

          evento.descripcion  = request.POST['descripcion']
          evento.linkDireccion  = request.POST['linkDireccion']
          evento.localidadAfectada  = request.POST['localidadAfectada']
          evento.tipoEvento  = request.POST['tipoEvento']
          evento.fechaDelEvento  = request.POST['fechaDelEvento']
          
          evento.nombreFuente  = request.POST['nombreFuente']
          
          evento.color  = request.POST['color']
          evento.tipo  = request.POST['tipo']
          
          evento.areaPimetAfectada  = request.POST['areaPimetAfectada']
          evento.lat   = request.POST['lat']
          evento.long  = request.POST['long']

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

    return render(request, "VerificacionesApp/nuevoEvento.html",  {'formset': formset, 'mensajeError':mensajeError})