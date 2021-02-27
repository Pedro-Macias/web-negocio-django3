from django.urls import path
from .import views


# crear las urls del blog

urlpatterns = [
    # packs blog
    path('', views.blog, name ='blog'),
    path('categoria/<int:categoria_id>/', views.categoria, name='categoria'),
    
]
