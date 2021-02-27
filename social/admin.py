from django.contrib import admin
from .models import Enlace
# Register your models here.
class EnlaceAdmin(admin.ModelAdmin):
    readonly_fields =('creado', 'modificado') 
    def get_readonly_fields(self, request , obj=None):
        if request.user.groups.filter(name='Personal').exists():
            return ('creado', 'modificado','clave','nombre')
        else:
            return('creado', 'modificado')


admin.site.register(Enlace, EnlaceAdmin)