from django.db import models
from django.contrib.auth.models import User
from productos.models import Producto
from decimal import Decimal

class Carrito(models.Model):
    """Carrito de compras"""
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    session_key = models.CharField(max_length=40, null=True, blank=True)
    
    # Timestamps
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Carrito'
        verbose_name_plural = 'Carritos'
    
    def __str__(self):
        if self.usuario:
            return f"Carrito de {self.usuario.username}"
        return f"Carrito anónimo ({self.session_key})"
    
    @property
    def total_items(self):
        """Cantidad total de items en el carrito"""
        return self.items.aggregate(
            total=models.Sum('cantidad')
        )['total'] or 0
    
    @property
    def subtotal(self):
        """Subtotal del carrito"""
        total = Decimal('0.00')
        for item in self.items.all():
            total += item.subtotal
        return total
    
    @property
    def total(self):
        """Total del carrito (por ahora igual al subtotal, luego se pueden agregar impuestos, descuentos, etc.)"""
        return self.subtotal
    
    def limpiar(self):
        """Vacía el carrito"""
        self.items.all().delete()

class ItemCarrito(models.Model):
    """Items individuales del carrito"""
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE, related_name='items')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Timestamps
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Item de Carrito'
        verbose_name_plural = 'Items de Carrito'
        unique_together = ['carrito', 'producto']
    
    def __str__(self):
        return f"{self.cantidad}x {self.producto.nombre}"
    
    @property
    def subtotal(self):
        """Subtotal del item"""
        if self.precio_unitario is None:
            return Decimal('0.00')
        return self.cantidad * self.precio_unitario
    
    def save(self, *args, **kwargs):
        # Guardar el precio actual del producto
        if not self.precio_unitario:
            self.precio_unitario = self.producto.precio_final
        super().save(*args, **kwargs)