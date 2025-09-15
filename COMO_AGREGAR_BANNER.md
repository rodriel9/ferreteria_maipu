# 🖼️ Cómo Agregar el Banner Principal de Ferretería Maipú

## 📋 Instrucciones Paso a Paso

### 1. 📸 Preparar la Imagen del Banner

**La imagen que me enviaste es perfecta para usar como banner principal.**

**Especificaciones recomendadas:**
- **Nombre del archivo:** `banner-principal.jpg`
- **Tamaño recomendado:** 1200x400 píxeles (o similar)
- **Formato:** JPG o PNG
- **Peso máximo:** 1MB

### 2. 📁 Ubicar el Archivo

1. **Guarda** tu imagen del banner (la que me enviaste)
2. **Renómbrala** a: `banner-principal.jpg`
3. **Cópiala** en la carpeta: `static/img/banner-principal.jpg`

**Ruta completa:** `ECOMMERCE_FERRETERIA/static/img/banner-principal.jpg`

### 3. ✅ Verificar que Funciona

1. **Reinicia** el servidor Django:
   - Para el servidor: `Ctrl+C`
   - Reinicia: `python manage.py runserver`

2. **Abre** tu navegador: http://127.0.0.1:8000/

3. **¡Deberías ver** tu banner ocupando todo el ancho de la página!

## 🎯 Lo que Verás Después

### ✅ En la Página Principal:
- **Banner completo** con tu imagen promocional
- **Información de contacto** debajo: 3794-001411
- **Dirección real:** Av. Maipú 255
- **Instagram:** @maipuferreteria
- **Horarios actualizados**

### 📱 Información Actualizada:
- ✅ Teléfono real: 3794-001411
- ✅ Instagram: @maipuferreteria  
- ✅ Dirección: Av. Maipú 255, Maipú
- ✅ Horarios: Lun-Sáb 08-13:30hs | 16-21:30hs, Dom 10-13:30hs

## 🔧 Si No Tienes la Imagen Aún

**El sitio está preparado con un fallback:**
- Si no hay imagen, mostrará un hero section con colores de tu marca
- Una vez que agregues `banner-principal.jpg`, aparecerá automáticamente

## 📐 Optimizar la Imagen

### Para Mejor Resultado:
1. **Redimensiona** a 1200x400 píxeles
2. **Optimiza** el peso (máximo 1MB)
3. **Asegúrate** que el texto se lea bien

### Herramientas Recomendadas:
- **Online:** Canva, Photopea, Squoosh
- **PC:** Paint, GIMP, Photoshop
- **Móvil:** Apps de edición de fotos

## 🎨 Personalización Adicional

### Si Quieres Cambiar el Tamaño:
En `templates/productos/home.html`, línea 10:
```html
<img src="{% static 'img/banner-principal.jpg' %}" alt="Ferretería Maipú - Banner Principal" class="img-fluid w-100" style="height: 400px; object-fit: cover;">
```

**Cambia `height: 400px`** por el tamaño que prefieras.

### Diferentes Imágenes por Sección:
Puedes crear:
- `banner-principal.jpg` - Página principal
- `banner-productos.jpg` - Para catálogo
- `banner-ofertas.jpg` - Para promociones

## 🚨 Solución de Problemas

### La imagen no aparece:
1. ✅ Verifica que se llame exactamente: `banner-principal.jpg`
2. ✅ Verifica que esté en: `static/img/banner-principal.jpg`
3. ✅ Reinicia el servidor Django
4. ✅ Recarga la página (Ctrl+F5)

### La imagen se ve cortada:
- Ajusta `height: 400px` a un valor mayor
- O redimensiona la imagen original

### La imagen se ve muy pesada:
- Comprime la imagen online
- Reduce la resolución si es muy grande

## 📱 Resultado Final

**Con tu banner integrado tendrás:**

✅ **Página principal impactante** con tu imagen promocional  
✅ **Información real** de contacto (3794-001411)  
✅ **Redes sociales** (@maipuferreteria)  
✅ **Horarios de atención** visibles  
✅ **Diseño profesional** con colores de tu marca  

## 🎯 Próximo Paso

1. **Guarda** tu imagen como `banner-principal.jpg`
2. **Cópiala** a `static/img/`
3. **Reinicia** el servidor
4. **¡Disfruta** tu ferretería online profesional!

---

**¡Tu banner quedará espectacular y muy profesional!** 🎉🔧