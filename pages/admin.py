from django.contrib import admin
from .models import Pagina
# Register your models here.
class PaginaAdmin(admin.ModelAdmin):
    readonly_fields =('creado', 'modificado') 


admin.site.register(Pagina, PaginaAdmin)