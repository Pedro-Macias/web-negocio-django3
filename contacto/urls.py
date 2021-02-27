from django.urls import path
from .import views


# crear las urls del contacto

urlpatterns = [
    # packs contacto
    path('', views.contact, name ='contact'),

]