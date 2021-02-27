from django.contrib import admin
from .models import Categoria , Entrada

# Register your models here.

class Categoria_fields (admin.ModelAdmin):
    readonly_fields =( 'creado','modificado')

class Entrada_fields (admin.ModelAdmin):
    readonly_fields =( 'creado','modificado')
    # personalizar entrada
    list_display = ('titulo', 'autor','publicado')
    ordering =('autor','publicado')
    # campo de busqueda
    search_fields= ('titulo','autor__username','categorias__nombre')
    # filtro
    list_filter =('categorias__nombre','autor__username',)

admin.site.register(Categoria, Categoria_fields)
admin.site.register(Entrada , Entrada_fields)