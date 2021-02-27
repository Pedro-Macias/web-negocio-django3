from django.urls import path
from .import views


# crear las urls del blog

urlpatterns = [
    # packs pages
    path('<int:pagina_id>/', views.pagina, name='pagina'),
    
]
