from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Pagina(models.Model):
    titulo = models.CharField( max_length= 200)
    contenido = RichTextField()
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name="Pagina"
        ordering =['titulo']

    def __str__(self):
        return self.titulo