# 🖼️ Cambiar Fondo a Imagen - Guía Simple

## 🎯 Objetivo
Cambiar el fondo rojo y negro por una imagen de tu ferretería.

## 🚀 2 Pasos Súper Fáciles:

### ✅ PASO 1: Preparar tu Imagen de Fondo
1. **Elige** una imagen que represente tu ferretería:
   - Foto del local
   - Productos organizados
   - Tu logo grande
   - Herramientas
2. **Guárdala** como `fondo-hero.jpg`
3. **Tamaño recomendado:** 1920x800 píxeles
4. **Peso máximo:** 1MB

### ✅ PASO 2: Copiar la Imagen
1. **Abre** la carpeta: `F:\pruebaG\nueva_forma\ECOMMERCE_FERRETERIA`
2. **Ve a:** `static` → `img`
3. **Pega** tu archivo `fondo-hero.jpg`

**Ruta final:** `F:\pruebaG\nueva_forma\ECOMMERCE_FERRETERIA\static\img\fondo-hero.jpg`

## 🔄 Ver el Resultado

1. **Recarga** la página: http://127.0.0.1:8000/
2. **¡Tu imagen aparecerá** como fondo!

## 🎨 Características del Fondo

**✅ Lo que tendrás:**
- Tu imagen como fondo del hero section
- Overlay oscuro para que el texto se lea bien
- Texto blanco sobre la imagen
- Efecto profesional

**✅ Si no hay imagen:**
- Mantiene el degradado rojo y negro actual
- No se rompe nada

## 🔧 Personalizar (Opcional)

### Cambiar la Opacidad del Overlay:
En `static/css/ferreteria-maipu.css`, línea 34:
```css
linear-gradient(rgba(33, 37, 41, 0.7), rgba(220, 53, 69, 0.8))
```
- Cambia `0.7` y `0.8` por valores menores (más claro) o mayores (más oscuro)

### Cambiar la Posición de la Imagen:
- `background-position: center;` → `background-position: top;` (arriba)
- `background-position: center;` → `background-position: bottom;` (abajo)

## 📸 Tipos de Imágenes Recomendadas

### ✅ Buenas opciones:
- Foto del frente de tu ferretería
- Estantes con herramientas organizadas
- Tu logo en grande con herramientas alrededor
- Productos destacados de tu ferretería

### ❌ Evitar:
- Imágenes muy oscuras
- Fotos con mucho texto
- Imágenes muy pequeñas o pixeladas

## 🚨 Si No Funciona

### Verifica:
- ✅ El archivo se llama exactamente: `fondo-hero.jpg`
- ✅ Está en: `static/img/fondo-hero.jpg`
- ✅ La imagen no es muy pesada (máximo 1MB)

### Reinicia:
- Recarga la página con `Ctrl+F5`
- Si no funciona, reinicia el servidor

## 🎯 Resultado Final

**Tendrás:**
- ✅ Tu imagen como fondo del hero
- ✅ Texto legible sobre la imagen
- ✅ Información de contacto visible
- ✅ Botones funcionales
- ✅ Diseño súper profesional

---

**¡Tu ferretería se verá increíble con tu propia imagen de fondo!** 📸🔧

**¿Ya tienes la imagen lista o necesitas ayuda para elegirla?** 🤔