from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    
    path('', views.inicio, name="Inicio"),
    path('nuevoEvento', views.nuevoEvento, name="NuevoEvento"),
  
 
    

    

]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)