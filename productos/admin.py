from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from .models import (
    Categoria, Marca, Producto, ImagenProducto, 
    Proveedor, ProductoProveedor
)

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'activa', 'orden', 'productos_count', 'creado']
    list_filter = ['activa', 'creado']
    search_fields = ['nombre', 'descripcion']
    prepopulated_fields = {'slug': ('nombre',)}
    list_editable = ['activa', 'orden']
    ordering = ['orden', 'nombre']
    
    def productos_count(self, obj):
        return obj.productos.count()
    productos_count.short_description = 'Productos'

@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'activa', 'productos_count', 'creado']
    list_filter = ['activa', 'creado']
    search_fields = ['nombre']
    prepopulated_fields = {'slug': ('nombre',)}
    list_editable = ['activa']
    
    def productos_count(self, obj):
        return obj.productos.count()
    productos_count.short_description = 'Productos'

class ImagenProductoInline(admin.TabularInline):
    model = ImagenProducto
    extra = 1
    fields = ['imagen', 'alt_text', 'orden', 'principal']

class ProductoProveedorInline(admin.TabularInline):
    model = ProductoProveedor
    extra = 1
    fields = ['proveedor', 'codigo_proveedor', 'precio_compra', 'tiempo_entrega', 'principal']

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = [
        'codigo', 'nombre', 'categoria', 'marca', 'precio_final_display', 
        'stock', 'estado', 'destacado', 'activo', 'creado'
    ]
    list_filter = [
        'categoria', 'marca', 'estado', 'destacado', 'activo', 
        'creado', 'stock_minimo'
    ]
    search_fields = ['nombre', 'codigo', 'codigo_barras', 'descripcion_corta']
    prepopulated_fields = {'slug': ('codigo', 'nombre')}
    list_editable = ['stock', 'destacado', 'activo']
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('nombre', 'slug', 'codigo', 'codigo_barras', 'categoria', 'marca')
        }),
        ('Descripción', {
            'fields': ('descripcion_corta', 'descripcion_larga', 'especificaciones')
        }),
        ('Precios', {
            'fields': ('precio', 'precio_oferta', 'costo')
        }),
        ('Inventario', {
            'fields': ('stock', 'stock_minimo')
        }),
        ('Medidas y Peso', {
            'fields': ('peso', 'largo', 'ancho', 'alto'),
            'classes': ('collapse',)
        }),
        ('Estado y Configuración', {
            'fields': ('estado', 'destacado', 'activo')
        }),
        ('SEO', {
            'fields': ('meta_title', 'meta_description'),
            'classes': ('collapse',)
        }),
    )
    
    inlines = [ImagenProductoInline, ProductoProveedorInline]
    
    actions = ['marcar_destacado', 'desmarcar_destacado', 'activar', 'desactivar']
    
    def precio_final_display(self, obj):
        if obj.tiene_oferta:
            return format_html(
                '<span style="text-decoration: line-through;">${}</span> <strong>${}</strong>',
                obj.precio, obj.precio_oferta
            )
        return f"${obj.precio}"
    precio_final_display.short_description = 'Precio'
    
    def marcar_destacado(self, request, queryset):
        queryset.update(destacado=True)
        self.message_user(request, f'{queryset.count()} productos marcados como destacados.')
    marcar_destacado.short_description = 'Marcar como destacado'
    
    def desmarcar_destacado(self, request, queryset):
        queryset.update(destacado=False)
        self.message_user(request, f'{queryset.count()} productos desmarcados como destacados.')
    desmarcar_destacado.short_description = 'Desmarcar como destacado'
    
    def activar(self, request, queryset):
        queryset.update(activo=True)
        self.message_user(request, f'{queryset.count()} productos activados.')
    activar.short_description = 'Activar productos'
    
    def desactivar(self, request, queryset):
        queryset.update(activo=False)
        self.message_user(request, f'{queryset.count()} productos desactivados.')
    desactivar.short_description = 'Desactivar productos'

@admin.register(ImagenProducto)
class ImagenProductoAdmin(admin.ModelAdmin):
    list_display = ['producto', 'imagen_thumbnail', 'alt_text', 'orden', 'principal', 'creado']
    list_filter = ['principal', 'creado']
    search_fields = ['producto__nombre', 'alt_text']
    list_editable = ['orden', 'principal']
    
    def imagen_thumbnail(self, obj):
        if obj.imagen:
            return format_html(
                '<img src="{}" width="50" height="50" style="object-fit: cover;" />',
                obj.imagen.url
            )
        return "Sin imagen"
    imagen_thumbnail.short_description = 'Vista previa'

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'razon_social', 'cuit', 'telefono', 'email', 'activo', 'productos_count']
    list_filter = ['activo', 'creado']
    search_fields = ['nombre', 'razon_social', 'cuit', 'email', 'contacto']
    list_editable = ['activo']
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('nombre', 'razon_social', 'cuit')
        }),
        ('Contacto', {
            'fields': ('telefono', 'email', 'direccion', 'contacto')
        }),
        ('Estado', {
            'fields': ('activo',)
        }),
    )
    
    def productos_count(self, obj):
        return obj.productos.count()
    productos_count.short_description = 'Productos'

@admin.register(ProductoProveedor)
class ProductoProveedorAdmin(admin.ModelAdmin):
    list_display = ['producto', 'proveedor', 'codigo_proveedor', 'precio_compra', 'tiempo_entrega', 'principal']
    list_filter = ['proveedor', 'principal', 'creado']
    search_fields = ['producto__nombre', 'proveedor__nombre', 'codigo_proveedor']
    list_editable = ['precio_compra', 'tiempo_entrega', 'principal']