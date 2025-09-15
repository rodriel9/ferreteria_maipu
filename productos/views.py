from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Producto, Categoria, Marca

def home(request):
    """Vista principal de la tienda"""
    # Productos destacados
    productos_destacados = Producto.objects.filter(
        destacado=True, 
        activo=True, 
        estado='disponible'
    )[:8]
    
    # Categorías principales
    categorias = Categoria.objects.filter(activa=True).order_by('orden')[:6]
    
    context = {
        'productos_destacados': productos_destacados,
        'categorias': categorias,
        'titulo': 'Ferretería Maipú - Todo para tu obra'
    }
    return render(request, 'productos/home.html', context)

def catalogo(request):
    """Vista del catálogo de productos"""
    productos = Producto.objects.filter(activo=True, estado='disponible')
    
    # Filtros
    categoria_id = request.GET.get('categoria')
    marca_id = request.GET.get('marca')
    buscar = request.GET.get('q')
    orden = request.GET.get('orden', 'nombre')
    
    if categoria_id:
        productos = productos.filter(categoria_id=categoria_id)
    
    if marca_id:
        productos = productos.filter(marca_id=marca_id)
    
    if buscar:
        productos = productos.filter(
            Q(nombre__icontains=buscar) |
            Q(descripcion_corta__icontains=buscar) |
            Q(codigo__icontains=buscar)
        )
    
    # Ordenamiento
    if orden == 'precio_asc':
        productos = productos.order_by('precio')
    elif orden == 'precio_desc':
        productos = productos.order_by('-precio')
    elif orden == 'nombre':
        productos = productos.order_by('nombre')
    elif orden == 'nuevo':
        productos = productos.order_by('-creado')
    
    # Paginación
    paginator = Paginator(productos, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Para los filtros
    categorias = Categoria.objects.filter(activa=True).order_by('nombre')
    marcas = Marca.objects.filter(activa=True).order_by('nombre')
    
    context = {
        'page_obj': page_obj,
        'categorias': categorias,
        'marcas': marcas,
        'categoria_actual': categoria_id,
        'marca_actual': marca_id,
        'buscar_actual': buscar or '',
        'orden_actual': orden,
        'titulo': 'Catálogo de Productos'
    }
    return render(request, 'productos/catalogo.html', context)

def detalle_producto(request, slug):
    """Vista de detalle de un producto"""
    producto = get_object_or_404(
        Producto, 
        slug=slug, 
        activo=True
    )
    
    # Productos relacionados (misma categoría)
    productos_relacionados = Producto.objects.filter(
        categoria=producto.categoria,
        activo=True,
        estado='disponible'
    ).exclude(id=producto.id)[:4]
    
    context = {
        'producto': producto,
        'productos_relacionados': productos_relacionados,
        'titulo': producto.nombre
    }
    return render(request, 'productos/detalle.html', context)

def categoria_detalle(request, slug):
    """Vista de productos por categoría"""
    categoria = get_object_or_404(Categoria, slug=slug, activa=True)
    
    productos = Producto.objects.filter(
        categoria=categoria,
        activo=True,
        estado='disponible'
    )
    
    # Ordenamiento
    orden = request.GET.get('orden', 'nombre')
    if orden == 'precio_asc':
        productos = productos.order_by('precio')
    elif orden == 'precio_desc':
        productos = productos.order_by('-precio')
    elif orden == 'nombre':
        productos = productos.order_by('nombre')
    elif orden == 'nuevo':
        productos = productos.order_by('-creado')
    
    # Paginación
    paginator = Paginator(productos, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'categoria': categoria,
        'page_obj': page_obj,
        'orden_actual': orden,
        'titulo': f'{categoria.nombre} - Productos'
    }
    return render(request, 'productos/categoria.html', context)