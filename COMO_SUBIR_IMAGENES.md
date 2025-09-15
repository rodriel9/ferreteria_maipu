# 📸 Cómo Subir Imágenes a Ferretería Maipú

## 🎯 Tipos de Imágenes que Puedes Subir

### 1. 🖼️ **Logo de la Ferretería**
- **Ubicación:** `static/img/logo-maipu.png`
- **Tamaño recomendado:** 200x200px
- **Formato:** PNG con fondo transparente

### 2. 📦 **Imágenes de Productos**
- **Ubicación:** `media/productos/`
- **Tamaño recomendado:** 800x800px
- **Formato:** JPG o PNG
- **Se suben desde el Panel de Administración**

## 🚀 Método 1: Subir Logo (Archivo Estático)

### Paso 1: Preparar tu Logo
1. **Redimensiona** tu logo a 200x200 píxeles
2. **Guárdalo** como `logo-maipu.png`
3. **Asegúrate** que tenga fondo transparente (PNG)

### Paso 2: Copiar a la Carpeta
1. Abre tu carpeta del proyecto: `ECOMMERCE_FERRETERIA`
2. Ve a: `static/img/`
3. Pega tu archivo: `logo-maipu.png`

### Paso 3: Activar el Logo
En `templates/base.html`, busca la línea 87:
```html
<!-- <img src="{% static 'img/logo-maipu.png' %}" alt="Ferretería Maipú" height="45" class="me-2"> -->
```

**Cámbiala por:**
```html
<img src="{% static 'img/logo-maipu.png' %}" alt="Ferretería Maipú" height="45" class="me-2">
```

Y comenta el placeholder:
```html
<!-- <div class="logo-placeholder d-inline-block">
    <i class="fas fa-tools text-danger"></i>
</div> -->
```

## 📦 Método 2: Subir Imágenes de Productos

### Opción A: Desde el Panel de Administración (Recomendado)

1. **Accede al Admin:** http://127.0.0.1:8000/admin/
2. **Login:** admin / admin123
3. **Ve a:** Productos → Productos
4. **Selecciona** un producto existente
5. **Scroll hacia abajo** hasta "Imágenes del producto"
6. **Haz clic** en "Agregar otra imagen del producto"
7. **Sube** tu imagen y guarda

### Opción B: Copiar Directamente (Más Rápido)

1. **Crea** la carpeta si no existe: `media/productos/`
2. **Copia** tus imágenes ahí
3. **Nombra** las imágenes descriptivamente:
   - `taladro-bosch-500w.jpg`
   - `martillo-stanley-16oz.jpg`
   - `destornillador-phillips-6mm.jpg`

### Opción C: Subir Múltiples Imágenes Rápido

**Estructura recomendada:**
```
media/
└── productos/
    ├── herramientas/
    │   ├── taladro-bosch.jpg
    │   ├── martillo-stanley.jpg
    │   └── destornillador-set.jpg
    ├── plomeria/
    │   ├── cano-pvc-110mm.jpg
    │   ├── codo-pvc-90grados.jpg
    │   └── llave-paso-1-2.jpg
    └── electricidad/
        ├── cable-tpg-2x1.jpg
        ├── enchufe-schuko.jpg
        └── interruptor-simple.jpg
```

## 🔧 Configurar Productos con Imágenes

### En el Panel de Administración:

1. **Ve a:** Productos → Productos
2. **Edita** un producto
3. **En "Imagen principal":** Sube la imagen principal
4. **En "Imágenes del producto":** Agrega imágenes adicionales
5. **Guarda** los cambios

### Campos importantes:
- **Imagen principal:** Se muestra en catálogo y detalle
- **Imágenes adicionales:** Galería en la página de detalle
- **Alt text:** Descripción para SEO y accesibilidad

## 📱 Optimización de Imágenes

### Tamaños Recomendados:
- **Logo:** 200x200px (PNG transparente)
- **Productos (principal):** 800x800px
- **Productos (galería):** 600x600px
- **Peso máximo:** 500KB por imagen

### Herramientas para Optimizar:
- **Online:** TinyPNG.com, Squoosh.app
- **Windows:** Paint, GIMP (gratis)
- **Móvil:** Apps de compresión de imágenes

## 🎨 Nombres de Archivos Recomendados

### ✅ Buenos Nombres:
- `logo-ferreteria-maipu.png`
- `taladro-bosch-gsb-500w.jpg`
- `martillo-carpintero-16oz.jpg`
- `pintura-latex-blanco-20lt.jpg`

### ❌ Evitar:
- `IMG_001.jpg`
- `photo123.png`
- `imagen sin nombre.jpg`
- `DSC_0001.JPG`

## 🔄 Actualizar Imágenes Existentes

### Si ya tienes productos sin imágenes:
1. **Identifica** productos sin imagen en el admin
2. **Busca** imágenes de esos productos
3. **Súbelas** usando el método preferido
4. **Asigna** las imágenes a los productos correctos

## 🚨 Solución de Problemas

### La imagen no aparece:
1. ✅ Verifica que el archivo esté en `media/productos/`
2. ✅ Revisa que el nombre no tenga espacios o caracteres especiales
3. ✅ Asegúrate que el formato sea JPG o PNG
4. ✅ Recarga la página (Ctrl+F5)

### La imagen se ve muy grande/pequeña:
- En el CSS puedes ajustar los tamaños
- Redimensiona la imagen original
- Usa herramientas de optimización

### Error de permisos:
- En Windows: Clic derecho → Propiedades → Seguridad
- Asegúrate que Django tenga permisos de escritura en `media/`

## 📊 Resultado Final

Después de subir las imágenes:
- ✅ Logo en el navbar
- ✅ Productos con imágenes atractivas
- ✅ Galería de imágenes en detalle de producto
- ✅ Catálogo visualmente mejorado
- ✅ Mejor experiencia de usuario

## 🎯 Próximos Pasos

1. **Sube tu logo** de Ferretería Maipú
2. **Agrega imágenes** a 10-15 productos principales
3. **Prueba** que todo se vea bien
4. **Optimiza** imágenes si es necesario
5. **¡Disfruta** tu ferretería online!

---

**¡Con imágenes tu ferretería se verá súper profesional!** 📸🔧