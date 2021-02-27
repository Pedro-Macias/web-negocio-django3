from django.urls import path
from .import views


# crear las urls del NUCLEO

urlpatterns = [
    # packs Nucleo
    path('', views.home, name ='home'),
    path('about/', views.about, name ='about'),
    path('visit/', views.visit, name ='visit'),

]