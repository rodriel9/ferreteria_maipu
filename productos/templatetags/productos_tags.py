from django import template
from productos.models import Categoria

register = template.Library()

@register.simple_tag
def get_categorias_activas():
    """Obtiene todas las categorías activas ordenadas"""
    return Categoria.objects.filter(activa=True).order_by('orden', 'nombre')

@register.filter
def subtract(value, arg):
    """Resta dos números"""
    try:
        return float(value) - float(arg)
    except (ValueError, TypeError):
        return 0