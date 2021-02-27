from django.shortcuts import render
from .models import Service

# Create your views here.
def services(request):
    #recuperar la base de datos
    servicios = Service.objects.all()
    return render(request, "Services/services.html",{'servicios': servicios})