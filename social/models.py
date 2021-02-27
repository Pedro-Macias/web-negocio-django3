from django.db import models

# Create your models here.
class Enlace(models.Model):
    clave = models.SlugField(verbose_name='Nombre Clave', max_length=100 , unique= True)
    nombre = models.CharField(verbose_name="Red Social", max_length= 200)
    url = models.URLField(verbose_name= 'Enlace', max_length = 200 , null= True , blank= True)
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name="Enlace"
        ordering =["nombre"]

    def __str__(self):
        return self.nombre