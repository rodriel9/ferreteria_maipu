# 🖼️ Agregar Tu Banner Promocional - PASOS EXACTOS

## 📸 Tu Imagen Promocional

**Tienes una imagen perfecta que incluye:**
- Logo de Ferretería Maipú
- Teléfono: 3794-001411
- Dirección: Av. Maipú 255
- Instagram: @maipuferreteria
- Horarios completos
- Marcas que trabajas

## 🚀 3 Pasos Exactos:

### ✅ PASO 1: Preparar la Imagen
1. **Encuentra** tu imagen promocional (la que me enviaste)
2. **Clic derecho** → "Guardar como..."
3. **Nómbrala:** `banner-principal.jpg`
4. **Guárdala** en el escritorio primero

### ✅ PASO 2: Copiar al Proyecto
1. **Abre** la carpeta: `F:\pruebaG\nueva_forma\ECOMMERCE_FERRETERIA`
2. **Ve a:** `static` → `img`
3. **Pega** el archivo `banner-principal.jpg`

**Ruta final:** `F:\pruebaG\nueva_forma\ECOMMERCE_FERRETERIA\static\img\banner-principal.jpg`

### ✅ PASO 3: Activar el Banner
**Necesitas editar 1 archivo:**

**Archivo:** `templates/productos/home.html`

**Busca la línea 9:**
```html
<div class="banner-fallback">
```

**Cámbiala por:**
```html
<div class="banner-fallback d-none">
```

**Busca las líneas 36-40:**
```html
<!--
<div class="banner-image-container">
    <img src="{% static 'img/banner-principal.jpg' %}" alt="Ferretería Maipú - Banner Principal" class="img-fluid w-100" style="height: 400px; object-fit: cover;">
</div>
-->
```

**Cámbiala por (quitar comentarios):**
```html
<div class="banner-image-container">
    <img src="{% static 'img/banner-principal.jpg' %}" alt="Ferretería Maipú - Banner Principal" class="img-fluid w-100" style="height: 400px; object-fit: cover;">
</div>
```

## 🔄 Ver el Resultado

1. **Guarda** el archivo
2. **Recarga** la página: http://127.0.0.1:8000/
3. **¡Tu banner aparecerá!**

## ✅ Resultado Final

**Tendrás:**
- ✅ Tu imagen promocional como banner principal
- ✅ Toda tu información visible
- ✅ Diseño súper profesional
- ✅ Colores de tu marca

---

**¿Necesitas que te ayude a hacer estos cambios paso a paso?** 🤔