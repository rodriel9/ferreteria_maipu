from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from productos.models import Producto
from .models import Carrito, ItemCarrito
import json

def obtener_carrito(request):
    """Obtiene o crea un carrito para el usuario o sesión actual"""
    if request.user.is_authenticated:
        carrito, created = Carrito.objects.get_or_create(usuario=request.user)
    else:
        session_key = request.session.session_key
        if not session_key:
            request.session.create()
            session_key = request.session.session_key
        carrito, created = Carrito.objects.get_or_create(session_key=session_key)
    return carrito

def ver_carrito(request):
    """Vista para mostrar el carrito de compras"""
    carrito = obtener_carrito(request)
    items = carrito.items.select_related('producto').all()
    
    context = {
        'carrito': carrito,
        'items': items,
        'titulo': 'Carrito de Compras'
    }
    return render(request, 'carrito/ver_carrito.html', context)

@require_POST
def agregar_producto(request, producto_id):
    """Agrega un producto al carrito"""
    try:
        producto = get_object_or_404(Producto, id=producto_id, activo=True)
        carrito = obtener_carrito(request)
        
        # Obtener cantidad del POST o usar 1 por defecto
        cantidad = int(request.POST.get('cantidad', 1))
        
        # Verificar stock disponible
        if cantidad > producto.stock:
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({
                    'success': False,
                    'message': f'Solo hay {producto.stock} unidades disponibles'
                })
            messages.error(request, f'Solo hay {producto.stock} unidades disponibles')
            return redirect('productos:detalle', slug=producto.slug)
        
        # Verificar si el producto ya está en el carrito
        item, created = ItemCarrito.objects.get_or_create(
            carrito=carrito,
            producto=producto,
            defaults={'cantidad': cantidad, 'precio_unitario': producto.precio_final}
        )
        
        if not created:
            # Si ya existe, aumentar la cantidad
            nueva_cantidad = item.cantidad + cantidad
            if nueva_cantidad > producto.stock:
                if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                    return JsonResponse({
                        'success': False,
                        'message': f'No puedes agregar más. Stock disponible: {producto.stock}'
                    })
                messages.error(request, f'No puedes agregar más. Stock disponible: {producto.stock}')
                return redirect('carrito:ver')
            
            item.cantidad = nueva_cantidad
            item.save()
        
        # Respuesta AJAX
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({
                'success': True,
                'message': f'{producto.nombre} agregado al carrito',
                'carrito_count': carrito.total_items,
                'carrito_total': str(carrito.total)
            })
        
        messages.success(request, f'{producto.nombre} agregado al carrito')
        return redirect('carrito:ver')
        
    except Exception as e:
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({
                'success': False,
                'message': 'Error al agregar el producto al carrito'
            })
        messages.error(request, 'Error al agregar el producto al carrito')
        return redirect('productos:home')

@require_POST
def actualizar_cantidad(request, item_id):
    """Actualiza la cantidad de un item en el carrito"""
    try:
        carrito = obtener_carrito(request)
        item = get_object_or_404(ItemCarrito, id=item_id, carrito=carrito)
        
        nueva_cantidad = int(request.POST.get('cantidad', 1))
        
        if nueva_cantidad <= 0:
            item.delete()
            message = f'{item.producto.nombre} eliminado del carrito'
        elif nueva_cantidad > item.producto.stock:
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({
                    'success': False,
                    'message': f'Solo hay {item.producto.stock} unidades disponibles'
                })
            messages.error(request, f'Solo hay {item.producto.stock} unidades disponibles')
            return redirect('carrito:ver')
        else:
            item.cantidad = nueva_cantidad
            item.save()
            message = f'Cantidad actualizada para {item.producto.nombre}'
        
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({
                'success': True,
                'message': message,
                'carrito_count': carrito.total_items,
                'carrito_total': str(carrito.total),
                'item_subtotal': str(item.subtotal) if nueva_cantidad > 0 else '0'
            })
        
        messages.success(request, message)
        return redirect('carrito:ver')
        
    except Exception as e:
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({
                'success': False,
                'message': 'Error al actualizar el carrito'
            })
        messages.error(request, 'Error al actualizar el carrito')
        return redirect('carrito:ver')

@require_POST
def eliminar_producto(request, item_id):
    """Elimina un producto del carrito"""
    try:
        carrito = obtener_carrito(request)
        item = get_object_or_404(ItemCarrito, id=item_id, carrito=carrito)
        producto_nombre = item.producto.nombre
        item.delete()
        
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({
                'success': True,
                'message': f'{producto_nombre} eliminado del carrito',
                'carrito_count': carrito.total_items,
                'carrito_total': str(carrito.total)
            })
        
        messages.success(request, f'{producto_nombre} eliminado del carrito')
        return redirect('carrito:ver')
        
    except Exception as e:
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({
                'success': False,
                'message': 'Error al eliminar el producto'
            })
        messages.error(request, 'Error al eliminar el producto')
        return redirect('carrito:ver')

@require_POST
def limpiar_carrito(request):
    """Limpia completamente el carrito"""
    try:
        carrito = obtener_carrito(request)
        carrito.limpiar()
        
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({
                'success': True,
                'message': 'Carrito limpiado',
                'carrito_count': 0,
                'carrito_total': '0'
            })
        
        messages.success(request, 'Carrito limpiado')
        return redirect('carrito:ver')
        
    except Exception as e:
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({
                'success': False,
                'message': 'Error al limpiar el carrito'
            })
        messages.error(request, 'Error al limpiar el carrito')
        return redirect('carrito:ver')

def carrito_count(request):
    """API endpoint para obtener la cantidad de items en el carrito"""
    carrito = obtener_carrito(request)
    return JsonResponse({
        'count': carrito.total_items,
        'total': str(carrito.total)
    })
