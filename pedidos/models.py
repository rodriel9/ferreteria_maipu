from django.db import models
from django.contrib.auth.models import User
from productos.models import Producto
from decimal import Decimal
import uuid

class Pedido(models.Model):
    """Pedidos de compra"""
    
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente de Pago'),
        ('pagado', 'Pagado'),
        ('procesando', 'Procesando'),
        ('enviado', 'Enviado'),
        ('entregado', 'Entregado'),
        ('cancelado', 'Cancelado'),
    ]
    
    METODO_PAGO_CHOICES = [
        ('stripe', 'Tarjeta de Crédito/Débito'),
        ('transferencia', 'Transferencia Bancaria'),
        ('efectivo', 'Efectivo'),
        ('mercadopago', 'Mercado Pago'),
    ]
    
    # Identificación
    numero = models.CharField(max_length=20, unique=True, editable=False)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    
    # Cliente
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pedidos')
    
    # Datos de facturación
    nombre_facturacion = models.CharField(max_length=100)
    apellido_facturacion = models.CharField(max_length=100)
    email_facturacion = models.EmailField()
    telefono_facturacion = models.CharField(max_length=20)
    direccion_facturacion = models.CharField(max_length=200)
    ciudad_facturacion = models.CharField(max_length=100)
    codigo_postal_facturacion = models.CharField(max_length=10)
    provincia_facturacion = models.CharField(max_length=100)
    
    # Datos de envío
    envio_diferente = models.BooleanField(default=False)
    nombre_envio = models.CharField(max_length=100, blank=True)
    apellido_envio = models.CharField(max_length=100, blank=True)
    direccion_envio = models.CharField(max_length=200, blank=True)
    ciudad_envio = models.CharField(max_length=100, blank=True)
    codigo_postal_envio = models.CharField(max_length=10, blank=True)
    provincia_envio = models.CharField(max_length=100, blank=True)
    
    # Montos
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    impuestos = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    costo_envio = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    descuento = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Estado y pago
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente')
    metodo_pago = models.CharField(max_length=20, choices=METODO_PAGO_CHOICES)
    pagado = models.BooleanField(default=False)
    fecha_pago = models.DateTimeField(null=True, blank=True)
    
    # IDs de transacciones externas
    stripe_payment_intent_id = models.CharField(max_length=200, blank=True)
    mercadopago_payment_id = models.CharField(max_length=200, blank=True)
    
    # Notas
    notas = models.TextField(blank=True, help_text="Notas adicionales del cliente")
    notas_internas = models.TextField(blank=True, help_text="Notas internas (no visibles para el cliente)")
    
    # Timestamps
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        ordering = ['-creado']
    
    def __str__(self):
        return f"Pedido #{self.numero} - {self.usuario.username}"
    
    def save(self, *args, **kwargs):
        if not self.numero:
            # Generar número de pedido único
            import datetime
            now = datetime.datetime.now()
            self.numero = f"PED{now.strftime('%Y%m%d')}{str(now.microsecond)[:3]}"
        super().save(*args, **kwargs)
    
    @property
    def nombre_completo_facturacion(self):
        return f"{self.nombre_facturacion} {self.apellido_facturacion}"
    
    @property
    def direccion_completa_facturacion(self):
        return f"{self.direccion_facturacion}, {self.ciudad_facturacion}, {self.provincia_facturacion} ({self.codigo_postal_facturacion})"
    
    @property
    def nombre_completo_envio(self):
        if self.envio_diferente:
            return f"{self.nombre_envio} {self.apellido_envio}"
        return self.nombre_completo_facturacion
    
    @property
    def direccion_completa_envio(self):
        if self.envio_diferente:
            return f"{self.direccion_envio}, {self.ciudad_envio}, {self.provincia_envio} ({self.codigo_postal_envio})"
        return self.direccion_completa_facturacion
    
    @property
    def puede_cancelar(self):
        """Indica si el pedido puede ser cancelado"""
        return self.estado in ['pendiente', 'pagado']
    
    def marcar_como_pagado(self):
        """Marca el pedido como pagado"""
        from django.utils import timezone
        self.pagado = True
        self.fecha_pago = timezone.now()
        if self.estado == 'pendiente':
            self.estado = 'pagado'
        self.save()

class ItemPedido(models.Model):
    """Items individuales de un pedido"""
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='items')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    
    # Datos del producto al momento de la compra (para mantener historial)
    nombre_producto = models.CharField(max_length=200)
    codigo_producto = models.CharField(max_length=50)
    
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        verbose_name = 'Item de Pedido'
        verbose_name_plural = 'Items de Pedido'
    
    def __str__(self):
        return f"{self.cantidad}x {self.nombre_producto}"
    
    def save(self, *args, **kwargs):
        # Guardar datos del producto y calcular subtotal
        if self.producto:
            self.nombre_producto = self.producto.nombre
            self.codigo_producto = self.producto.codigo
        
        self.subtotal = self.cantidad * self.precio_unitario
        super().save(*args, **kwargs)

class EstadoPedido(models.Model):
    """Historial de estados de pedidos"""
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='historial_estados')
    estado = models.CharField(max_length=20, choices=Pedido.ESTADO_CHOICES)
    comentario = models.TextField(blank=True)
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, help_text="Usuario que cambió el estado")
    
    # Timestamp
    creado = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Estado de Pedido'
        verbose_name_plural = 'Estados de Pedidos'
        ordering = ['-creado']
    
    def __str__(self):
        return f"Pedido #{self.pedido.numero} - {self.get_estado_display()}"