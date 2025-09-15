from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from .models import Pedido, ItemPedido, EstadoPedido

class ItemPedidoInline(admin.TabularInline):
    model = ItemPedido
    extra = 0
    readonly_fields = ['subtotal']
    fields = ['producto', 'nombre_producto', 'codigo_producto', 'cantidad', 'precio_unitario', 'subtotal']

class EstadoPedidoInline(admin.TabularInline):
    model = EstadoPedido
    extra = 1
    fields = ['estado', 'comentario', 'usuario']

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = [
        'numero', 'usuario', 'nombre_completo_facturacion', 'total', 
        'estado', 'metodo_pago', 'pagado', 'creado'
    ]
    list_filter = ['estado', 'metodo_pago', 'pagado', 'creado', 'envio_diferente']
    search_fields = [
        'numero', 'usuario__username', 'usuario__email',
        'nombre_facturacion', 'apellido_facturacion', 'email_facturacion'
    ]
    readonly_fields = ['numero', 'uuid', 'subtotal', 'total', 'creado', 'actualizado']
    list_editable = ['estado']
    
    fieldsets = (
        ('Información del Pedido', {
            'fields': ('numero', 'uuid', 'usuario', 'estado', 'notas', 'notas_internas')
        }),
        ('Datos de Facturación', {
            'fields': (
                'nombre_facturacion', 'apellido_facturacion', 'email_facturacion', 'telefono_facturacion',
                'direccion_facturacion', 'ciudad_facturacion', 'codigo_postal_facturacion', 'provincia_facturacion'
            )
        }),
        ('Datos de Envío', {
            'fields': (
                'envio_diferente', 'nombre_envio', 'apellido_envio',
                'direccion_envio', 'ciudad_envio', 'codigo_postal_envio', 'provincia_envio'
            ),
            'classes': ('collapse',)
        }),
        ('Montos', {
            'fields': ('subtotal', 'impuestos', 'costo_envio', 'descuento', 'total')
        }),
        ('Pago', {
            'fields': (
                'metodo_pago', 'pagado', 'fecha_pago',
                'stripe_payment_intent_id', 'mercadopago_payment_id'
            )
        }),
        ('Timestamps', {
            'fields': ('creado', 'actualizado'),
            'classes': ('collapse',)
        }),
    )
    
    inlines = [ItemPedidoInline, EstadoPedidoInline]
    
    actions = ['marcar_como_pagado', 'marcar_como_procesando', 'marcar_como_enviado']
    
    def marcar_como_pagado(self, request, queryset):
        count = 0
        for pedido in queryset:
            if pedido.estado == 'pendiente':
                pedido.marcar_como_pagado()
                count += 1
        self.message_user(request, f'{count} pedidos marcados como pagados.')
    marcar_como_pagado.short_description = 'Marcar como pagado'
    
    def marcar_como_procesando(self, request, queryset):
        queryset.update(estado='procesando')
        self.message_user(request, f'{queryset.count()} pedidos marcados como procesando.')
    marcar_como_procesando.short_description = 'Marcar como procesando'
    
    def marcar_como_enviado(self, request, queryset):
        queryset.update(estado='enviado')
        self.message_user(request, f'{queryset.count()} pedidos marcados como enviados.')
    marcar_como_enviado.short_description = 'Marcar como enviado'

@admin.register(ItemPedido)
class ItemPedidoAdmin(admin.ModelAdmin):
    list_display = ['pedido', 'nombre_producto', 'codigo_producto', 'cantidad', 'precio_unitario', 'subtotal']
    list_filter = ['pedido__estado', 'pedido__creado']
    search_fields = ['pedido__numero', 'nombre_producto', 'codigo_producto']
    readonly_fields = ['subtotal']

@admin.register(EstadoPedido)
class EstadoPedidoAdmin(admin.ModelAdmin):
    list_display = ['pedido', 'estado', 'usuario', 'creado']
    list_filter = ['estado', 'creado']
    search_fields = ['pedido__numero', 'comentario']
    readonly_fields = ['creado']