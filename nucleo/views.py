from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.


def home(request):
    return render(request, "nucleo/home.html")

def about(request):
    return render(request, "nucleo/about.html")

def visit(request):
    return render(request, "nucleo/visit.html")


    




