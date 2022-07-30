
from django.template.defaultfilters import slugify


from django.db import models

# Create your models here.



class Evento(models.Model):
    

    creacion= models.DateTimeField(auto_now_add=True)
    
    #Sobre el evento
    descripcion = models.TextField(null=False, blank=False)
    linkDireccion = models.CharField(max_length=200)
    localidadAfectada  = models.CharField(max_length=200)
    tipoEvento = models.CharField(max_length=200,null=False, blank=False)
    fechaDelEvento = models.DateField(null=False, blank=False)
    
    #Sobre la fuente
    nombreFuente  = models.CharField(max_length=200)
    
    #Sobre alertas
    color= models.CharField(max_length=50, null=False, blank=False)
    tipo= models.CharField(max_length=50, null=False, blank=False)
    
    #Geografico
    areaPimetAfectada = models.CharField(max_length=200,null=False, blank=False)
    lat = models.FloatField(null=False, blank=False)
    long = models.FloatField(null=False, blank=False)
    #puntoRepresentativo = models.PointField()

    def __str__(self):
        return f"{self.fechaDelEvento} --  {self.tipoEvento} -- {self.localidadAfectada} -- {self.nombreFuente}"
    
    
def get_image_filename(instance, filename):
    title =  'titulo'
    slug = slugify(title)
    return "imagenesEventos/%s-%s" % (slug, filename)  
    
class Imagen(models.Model):

    #img = models.ImageField(upload_to='imagenesArboles')
    

    #relacion
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, null=True,blank=True)
    image = models.ImageField(null=True, blank=True, upload_to=get_image_filename,verbose_name='Image')

    def __str__(self):
        return '%s;%s;%s' %(self.pk, self.image, self.evento.pk)

    class Meta:
        verbose_name = "Imagen"
        verbose_name_plural ="Imagenes"