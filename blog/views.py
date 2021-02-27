from django.shortcuts import render , get_object_or_404
from .models import Entrada, Categoria

# Create your views here.
def blog(request):
    entradas = Entrada.objects.all()
    return render(request, "blog/blog.html", {'entradas':entradas})

def categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id = categoria_id)
    # forma rudimentaria
    # entradas = Entrada.objects.filter(categorias = categoria)
    return render(request,"blog/categoria.html", {'categoria':categoria})
    

