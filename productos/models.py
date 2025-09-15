from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class Categoria(models.Model):
    """Categorías de productos de ferretería"""
    nombre = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    descripcion = models.TextField(blank=True)
    imagen = models.ImageField(upload_to='categorias/', blank=True, null=True)
    activa = models.BooleanField(default=True)
    orden = models.PositiveIntegerField(default=0)
    
    # Timestamps
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['orden', 'nombre']
    
    def __str__(self):
        return self.nombre
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('productos:categoria', kwargs={'slug': self.slug})

class Marca(models.Model):
    """Marcas de productos"""
    nombre = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    logo = models.ImageField(upload_to='marcas/', blank=True, null=True)
    activa = models.BooleanField(default=True)
    
    # Timestamps
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'
        ordering = ['nombre']
    
    def __str__(self):
        return self.nombre
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)
        super().save(*args, **kwargs)

class Producto(models.Model):
    """Productos de ferretería"""
    
    ESTADO_CHOICES = [
        ('disponible', 'Disponible'),
        ('agotado', 'Agotado'),
        ('descontinuado', 'Descontinuado'),
    ]
    
    # Información básica
    nombre = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    codigo = models.CharField(max_length=50, unique=True, help_text="Código interno del producto")
    codigo_barras = models.CharField(max_length=50, blank=True, help_text="Código de barras")
    
    # Relaciones
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos')
    marca = models.ForeignKey(Marca, on_delete=models.SET_NULL, null=True, blank=True, related_name='productos')
    
    # Descripción
    descripcion_corta = models.TextField(max_length=500, help_text="Descripción breve para listados")
    descripcion_larga = models.TextField(blank=True, help_text="Descripción detallada")
    especificaciones = models.JSONField(default=dict, blank=True, help_text="Especificaciones técnicas")
    
    # Precios
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    precio_oferta = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    costo = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, help_text="Costo del producto")
    
    # Inventario
    stock = models.PositiveIntegerField(default=0)
    stock_minimo = models.PositiveIntegerField(default=5, help_text="Alerta cuando el stock esté por debajo de este valor")
    
    # Medidas y peso
    peso = models.DecimalField(max_digits=8, decimal_places=3, null=True, blank=True, help_text="Peso en kg")
    largo = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True, help_text="Largo en cm")
    ancho = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True, help_text="Ancho en cm")
    alto = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True, help_text="Alto en cm")
    
    # Estado y configuración
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='disponible')
    destacado = models.BooleanField(default=False, help_text="Mostrar en productos destacados")
    activo = models.BooleanField(default=True)
    
    # SEO
    meta_title = models.CharField(max_length=200, blank=True)
    meta_description = models.CharField(max_length=300, blank=True)
    
    # Timestamps
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['-creado']
        indexes = [
            models.Index(fields=['codigo']),
            models.Index(fields=['categoria', 'activo']),
            models.Index(fields=['destacado', 'activo']),
        ]
    
    def __str__(self):
        return f"{self.codigo} - {self.nombre}"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.codigo}-{self.nombre}")
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('productos:detalle', kwargs={'slug': self.slug})
    
    @property
    def precio_final(self):
        """Retorna el precio de oferta si existe, sino el precio normal"""
        return self.precio_oferta if self.precio_oferta else self.precio
    
    @property
    def tiene_oferta(self):
        """Indica si el producto tiene precio de oferta"""
        return self.precio_oferta is not None and self.precio_oferta < self.precio
    
    @property
    def descuento_porcentaje(self):
        """Calcula el porcentaje de descuento"""
        if self.tiene_oferta:
            return round(((self.precio - self.precio_oferta) / self.precio) * 100)
        return 0
    
    @property
    def disponible(self):
        """Indica si el producto está disponible"""
        return self.activo and self.estado == 'disponible' and self.stock > 0
    
    @property
    def stock_bajo(self):
        """Indica si el stock está por debajo del mínimo"""
        return self.stock <= self.stock_minimo

class ImagenProducto(models.Model):
    """Imágenes de productos"""
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='imagenes')
    imagen = models.ImageField(upload_to='productos/')
    alt_text = models.CharField(max_length=200, blank=True)
    orden = models.PositiveIntegerField(default=0)
    principal = models.BooleanField(default=False, help_text="Imagen principal del producto")
    
    # Timestamps
    creado = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Imagen de Producto'
        verbose_name_plural = 'Imágenes de Productos'
        ordering = ['orden', '-principal']
    
    def __str__(self):
        return f"Imagen de {self.producto.nombre}"
    
    def save(self, *args, **kwargs):
        # Si es la imagen principal, desmarcar las demás
        if self.principal:
            ImagenProducto.objects.filter(producto=self.producto, principal=True).update(principal=False)
        super().save(*args, **kwargs)

class Proveedor(models.Model):
    """Proveedores de productos"""
    nombre = models.CharField(max_length=200)
    razon_social = models.CharField(max_length=200, blank=True)
    cuit = models.CharField(max_length=15, blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    direccion = models.TextField(blank=True)
    contacto = models.CharField(max_length=200, blank=True, help_text="Nombre del contacto principal")
    activo = models.BooleanField(default=True)
    
    # Timestamps
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
        ordering = ['nombre']
    
    def __str__(self):
        return self.nombre

class ProductoProveedor(models.Model):
    """Relación entre productos y proveedores con precios"""
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='proveedores')
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, related_name='productos')
    codigo_proveedor = models.CharField(max_length=100, blank=True, help_text="Código del producto según el proveedor")
    precio_compra = models.DecimalField(max_digits=10, decimal_places=2)
    tiempo_entrega = models.PositiveIntegerField(null=True, blank=True, help_text="Días de entrega")
    principal = models.BooleanField(default=False, help_text="Proveedor principal para este producto")
    
    # Timestamps
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Producto-Proveedor'
        verbose_name_plural = 'Productos-Proveedores'
        unique_together = ['producto', 'proveedor']
    
    def __str__(self):
        return f"{self.producto.nombre} - {self.proveedor.nombre}"