from django.urls import path
from .import views


# crear las urls del NUCLEO

urlpatterns = [
    # packs Services
    path('', views.services, name ='services'),


]