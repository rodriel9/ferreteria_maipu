#!/usr/bin/env python
"""
Script para crear datos de ejemplo para la ferretería
Ejecutar con: python manage.py shell < crear_datos_ejemplo.py
"""

import os
import django
from decimal import Decimal

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ferreteria_ecommerce.settings')
django.setup()

from productos.models import Categoria, Marca, Producto, Proveedor

def crear_datos_ejemplo():
    print("🏗️ Creando datos de ejemplo para Ferretería Maipú...")
    
    # Crear categorías
    categorias_data = [
        {
            'nombre': 'Herramientas Manuales',
            'descripcion': 'Martillos, destornilladores, llaves, alicates y más',
            'orden': 1
        },
        {
            'nombre': 'Herramientas Eléctricas',
            'descripcion': 'Taladros, sierras, amoladoras y herramientas a batería',
            'orden': 2
        },
        {
            'nombre': 'Materiales de Construcción',
            'descripcion': 'Cemento, ladrillos, arena, piedra y materiales básicos',
            'orden': 3
        },
        {
            'nombre': 'Tornillería y Fijaciones',
            'descripcion': 'Tornillos, tuercas, arandelas, clavos y sistemas de fijación',
            'orden': 4
        },
        {
            'nombre': 'Plomería',
            'descripcion': 'Tuberías, conexiones, grifería y accesorios de plomería',
            'orden': 5
        },
        {
            'nombre': 'Electricidad',
            'descripcion': 'Cables, interruptores, enchufes y material eléctrico',
            'orden': 6
        },
        {
            'nombre': 'Pinturas y Barnices',
            'descripcion': 'Pinturas, barnices, pinceles y accesorios para pintura',
            'orden': 7
        },
        {
            'nombre': 'Ferretería General',
            'descripcion': 'Candados, cadenas, bisagras y accesorios diversos',
            'orden': 8
        }
    ]
    
    categorias = {}
    for cat_data in categorias_data:
        categoria, created = Categoria.objects.get_or_create(
            nombre=cat_data['nombre'],
            defaults=cat_data
        )
        categorias[cat_data['nombre']] = categoria
        if created:
            print(f"✅ Categoría creada: {categoria.nombre}")
    
    # Crear marcas
    marcas_data = [
        'Stanley', 'DeWalt', 'Bosch', 'Makita', 'Black & Decker',
        'Irwin', 'Klein Tools', 'Craftsman', 'Ridgid', 'Milwaukee',
        'Truper', 'Bahco', 'Gedore', 'Tramontina', 'Bellota'
    ]
    
    marcas = {}
    for marca_nombre in marcas_data:
        marca, created = Marca.objects.get_or_create(
            nombre=marca_nombre
        )
        marcas[marca_nombre] = marca
        if created:
            print(f"✅ Marca creada: {marca.nombre}")
    
    # Crear proveedores
    proveedores_data = [
        {
            'nombre': 'Distribuidora Ferretera S.A.',
            'razon_social': 'Distribuidora Ferretera Sociedad Anónima',
            'cuit': '30-12345678-9',
            'telefono': '+54 11 4567-8900',
            'email': 'ventas@distferretera.com.ar',
            'contacto': 'Juan Pérez'
        },
        {
            'nombre': 'Herramientas del Norte',
            'razon_social': 'Herramientas del Norte SRL',
            'cuit': '30-87654321-0',
            'telefono': '+54 11 4321-0987',
            'email': 'info@herramientasnorte.com',
            'contacto': 'María González'
        }
    ]
    
    proveedores = {}
    for prov_data in proveedores_data:
        proveedor, created = Proveedor.objects.get_or_create(
            nombre=prov_data['nombre'],
            defaults=prov_data
        )
        proveedores[prov_data['nombre']] = proveedor
        if created:
            print(f"✅ Proveedor creado: {proveedor.nombre}")
    
    # Crear productos de ejemplo
    productos_data = [
        # Herramientas Manuales
        {
            'nombre': 'Martillo de Carpintero 16oz',
            'codigo': 'MART001',
            'categoria': 'Herramientas Manuales',
            'marca': 'Stanley',
            'descripcion_corta': 'Martillo de carpintero con mango de madera, cabeza de acero forjado',
            'descripcion_larga': 'Martillo profesional para carpintería con cabeza de acero forjado de alta calidad. Mango ergonómico de madera que absorbe las vibraciones. Peso: 16oz (450g). Ideal para trabajos de construcción y carpintería.',
            'precio': Decimal('8500.00'),
            'stock': 25,
            'destacado': True,
            'especificaciones': {
                'peso': '450g',
                'material_cabeza': 'Acero forjado',
                'material_mango': 'Madera',
                'longitud': '33cm'
            }
        },
        {
            'nombre': 'Juego de Destornilladores 6 piezas',
            'codigo': 'DEST001',
            'categoria': 'Herramientas Manuales',
            'marca': 'Stanley',
            'descripcion_corta': 'Juego de 6 destornilladores Phillips y planos, mangos ergonómicos',
            'descripcion_larga': 'Set completo de destornilladores profesionales. Incluye 3 destornilladores planos y 3 Phillips de diferentes medidas. Mangos ergonómicos con grip antideslizante.',
            'precio': Decimal('12500.00'),
            'stock': 15,
            'destacado': True
        },
        {
            'nombre': 'Llave Inglesa Ajustable 10"',
            'codigo': 'LLAV001',
            'categoria': 'Herramientas Manuales',
            'marca': 'Bahco',
            'descripcion_corta': 'Llave inglesa ajustable de 10 pulgadas, acero cromo vanadio',
            'descripcion_larga': 'Llave inglesa profesional fabricada en acero cromo vanadio. Apertura máxima de 32mm. Mandíbulas templadas y rectificadas para mayor durabilidad.',
            'precio': Decimal('15800.00'),
            'stock': 20
        },
        
        # Herramientas Eléctricas
        {
            'nombre': 'Taladro Percutor 13mm 650W',
            'codigo': 'TAL001',
            'categoria': 'Herramientas Eléctricas',
            'marca': 'Bosch',
            'descripcion_corta': 'Taladro percutor profesional 650W, mandril 13mm, velocidad variable',
            'descripcion_larga': 'Taladro percutor de alto rendimiento con motor de 650W. Mandril de 13mm con cierre automático. Velocidad variable y función percusión para trabajos en mampostería.',
            'precio': Decimal('45900.00'),
            'precio_oferta': Decimal('39900.00'),
            'stock': 8,
            'destacado': True,
            'especificaciones': {
                'potencia': '650W',
                'mandril': '13mm',
                'velocidad_max': '3000 rpm',
                'percusion': 'Sí'
            }
        },
        {
            'nombre': 'Amoladora Angular 115mm 850W',
            'codigo': 'AMO001',
            'categoria': 'Herramientas Eléctricas',
            'marca': 'DeWalt',
            'descripcion_corta': 'Amoladora angular 4.5", motor 850W, empuñadura lateral',
            'descripcion_larga': 'Amoladora angular profesional con disco de 115mm (4.5"). Motor de 850W de alta potencia. Incluye empuñadura lateral y protector de disco.',
            'precio': Decimal('38500.00'),
            'stock': 12
        },
        
        # Tornillería
        {
            'nombre': 'Tornillos Autoperforantes 8x1" (100 unidades)',
            'codigo': 'TORN001',
            'categoria': 'Tornillería y Fijaciones',
            'marca': 'Tramontina',
            'descripcion_corta': 'Tornillos autoperforantes para chapa, cabeza Phillips, 100 unidades',
            'descripcion_larga': 'Tornillos autoperforantes de alta calidad para fijación en chapa y perfiles metálicos. Cabeza Phillips, punta autoperforante. Caja de 100 unidades.',
            'precio': Decimal('2800.00'),
            'stock': 50,
            'especificaciones': {
                'medida': '8 x 1"',
                'material': 'Acero zincado',
                'cabeza': 'Phillips',
                'cantidad': '100 unidades'
            }
        },
        {
            'nombre': 'Clavos de Acero 2" (1kg)',
            'codigo': 'CLAV001',
            'categoria': 'Tornillería y Fijaciones',
            'marca': 'Bellota',
            'descripcion_corta': 'Clavos de acero común 2 pulgadas, bolsa de 1kg',
            'descripcion_larga': 'Clavos de acero común de 2 pulgadas para construcción general. Bolsa de 1kg aproximadamente 180 unidades.',
            'precio': Decimal('1850.00'),
            'stock': 30
        },
        
        # Plomería
        {
            'nombre': 'Caño PVC 110mm x 3m',
            'codigo': 'PVC001',
            'categoria': 'Plomería',
            'descripcion_corta': 'Caño PVC para desagües, diámetro 110mm, longitud 3 metros',
            'descripcion_larga': 'Tubo de PVC rígido para instalaciones de desagües cloacales. Diámetro 110mm, longitud 3 metros. Cumple normas IRAM.',
            'precio': Decimal('3200.00'),
            'stock': 40
        },
        
        # Electricidad
        {
            'nombre': 'Cable Unipolar 2.5mm x 100m',
            'codigo': 'CAB001',
            'categoria': 'Electricidad',
            'descripcion_corta': 'Cable unipolar 2.5mm², rollo de 100 metros, color azul',
            'descripcion_larga': 'Cable unipolar de cobre 2.5mm² para instalaciones eléctricas domiciliarias. Aislación PVC. Rollo de 100 metros.',
            'precio': Decimal('18500.00'),
            'stock': 15,
            'especificaciones': {
                'seccion': '2.5mm²',
                'material': 'Cobre',
                'aislacion': 'PVC',
                'longitud': '100m'
            }
        },
        
        # Pinturas
        {
            'nombre': 'Pintura Látex Interior Blanco 20L',
            'codigo': 'PINT001',
            'categoria': 'Pinturas y Barnices',
            'descripcion_corta': 'Pintura látex acrílico para interiores, color blanco, balde 20 litros',
            'descripcion_larga': 'Pintura látex acrílico de primera calidad para paredes interiores. Excelente cubrimiento y lavabilidad. Balde de 20 litros.',
            'precio': Decimal('24500.00'),
            'stock': 10,
            'destacado': True
        }
    ]
    
    for prod_data in productos_data:
        categoria = categorias.get(prod_data['categoria'])
        marca = marcas.get(prod_data.get('marca')) if prod_data.get('marca') else None
        
        producto_data = {
            'nombre': prod_data['nombre'],
            'codigo': prod_data['codigo'],
            'categoria': categoria,
            'marca': marca,
            'descripcion_corta': prod_data['descripcion_corta'],
            'descripcion_larga': prod_data.get('descripcion_larga', ''),
            'precio': prod_data['precio'],
            'precio_oferta': prod_data.get('precio_oferta'),
            'stock': prod_data['stock'],
            'destacado': prod_data.get('destacado', False),
            'especificaciones': prod_data.get('especificaciones', {})
        }
        
        producto, created = Producto.objects.get_or_create(
            codigo=prod_data['codigo'],
            defaults=producto_data
        )
        
        if created:
            print(f"✅ Producto creado: {producto.codigo} - {producto.nombre}")
    
    print("\n🎉 ¡Datos de ejemplo creados exitosamente!")
    print(f"📊 Resumen:")
    print(f"   - Categorías: {Categoria.objects.count()}")
    print(f"   - Marcas: {Marca.objects.count()}")
    print(f"   - Productos: {Producto.objects.count()}")
    print(f"   - Proveedores: {Proveedor.objects.count()}")

if __name__ == "__main__":
    crear_datos_ejemplo()