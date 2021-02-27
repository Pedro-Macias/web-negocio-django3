from django.shortcuts import render , get_object_or_404
from .models import Pagina

# Create your views here.
def pagina(request, pagina_id):
    pagina = get_object_or_404(Pagina, id= pagina_id)
    return render(request,'pages/sample.html', {'pagina':pagina})