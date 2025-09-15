from django.contrib import admin
from django.utils.html import format_html
from .models import Carrito, ItemCarrito

class ItemCarritoInline(admin.TabularInline):
    model = ItemCarrito
    extra = 0
    readonly_fields = ['subtotal']
    fields = ['producto', 'cantidad', 'precio_unitario', 'subtotal']

@admin.register(Carrito)
class CarritoAdmin(admin.ModelAdmin):
    list_display = ['id', 'usuario_display', 'session_key_short', 'total_items', 'total_display', 'creado']
    list_filter = ['creado', 'actualizado']
    search_fields = ['usuario__username', 'usuario__email', 'session_key']
    readonly_fields = ['total_items', 'subtotal', 'total', 'creado', 'actualizado']
    
    inlines = [ItemCarritoInline]
    
    actions = ['limpiar_carritos']
    
    def usuario_display(self, obj):
        if obj.usuario:
            return f"{obj.usuario.username} ({obj.usuario.email})"
        return "Usuario Anónimo"
    usuario_display.short_description = 'Usuario'
    
    def session_key_short(self, obj):
        if obj.session_key:
            return f"{obj.session_key[:8]}..."
        return "-"
    session_key_short.short_description = 'Sesión'
    
    def total_display(self, obj):
        return format_html('<strong>${}</strong>', obj.total)
    total_display.short_description = 'Total'
    
    def limpiar_carritos(self, request, queryset):
        for carrito in queryset:
            carrito.limpiar()
        self.message_user(request, f'{queryset.count()} carritos limpiados.')
    limpiar_carritos.short_description = 'Limpiar carritos seleccionados'

@admin.register(ItemCarrito)
class ItemCarritoAdmin(admin.ModelAdmin):
    list_display = ['id', 'carrito_usuario', 'producto', 'cantidad', 'precio_unitario', 'subtotal_display', 'creado']
    list_filter = ['creado', 'actualizado']
    search_fields = ['producto__nombre', 'producto__codigo', 'carrito__usuario__username']
    readonly_fields = ['subtotal', 'creado', 'actualizado']
    
    def carrito_usuario(self, obj):
        if obj.carrito.usuario:
            return obj.carrito.usuario.username
        return f"Anónimo ({obj.carrito.session_key[:8]}...)" if obj.carrito.session_key else "Anónimo"
    carrito_usuario.short_description = 'Usuario del Carrito'
    
    def subtotal_display(self, obj):
        return format_html('<strong>${}</strong>', obj.subtotal)
    subtotal_display.short_description = 'Subtotal'