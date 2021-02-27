from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name="categoria"
        ordering =["-creado"]

    def __str__(self):
        return self.nombre
    

class Entrada(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = RichTextField()
    publicado = models.DateTimeField(verbose_name='Fecha Publicacion', default=now)
    imagen = models.ImageField(upload_to='blog',null=True, blank=True)
    # lo importamos del modelo user
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    # Relacionar dos modelos pero eligiendo varias categorias
    categorias = models.ManyToManyField(Categoria, related_name='get_entradas')
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name="Entrada"
        ordering =["-creado"]

    def __str__(self):
        return self.titulo
