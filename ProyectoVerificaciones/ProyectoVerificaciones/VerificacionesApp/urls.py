from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    
    path('inicio', views.inicio, name="Inicio"),
    path('nuevoEvento', views.nuevoEvento, name="NuevoEvento"),
    path('todosLosEventos', views.todosLosEventos, name="TodosLosEventos"),
    path('eventosPorFecha', views.eventosPorFecha, name="EventosPorFecha"),
    path('eventosEntreFechas', views.eventosEntreFechas, name="EventosEntreFechas"),
   
  
 
    

]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)