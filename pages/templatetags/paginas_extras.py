from django import template
from pages.models import Pagina


# registrar en la libreria de templates

register= template.Library()

@register.simple_tag
def get_lista_paginas():
    paginas = Pagina.objects.all()
    return paginas