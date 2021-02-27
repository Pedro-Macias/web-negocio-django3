from .models import Enlace

# procesador de contextos
def contexto_dict(request):
    contexto ={}
    enlaces = Enlace.objects.all()
    for enlace in enlaces:
        contexto[enlace.clave] = enlace.url
    return contexto
