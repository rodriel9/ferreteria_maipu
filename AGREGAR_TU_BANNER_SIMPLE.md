# 🖼️ Cómo Agregar TU Banner en 3 Pasos Simples

## 📸 Tu Imagen Promocional

**La imagen que me enviaste es perfecta para usar como banner.**

## 🚀 3 Pasos Súper Fáciles:

### ✅ Paso 1: Preparar la Imagen
1. **Guarda** tu imagen promocional (la que me enviaste)
2. **Renómbrala** exactamente a: `banner-principal.jpg`
3. **Ubicación:** Debe quedar en tu escritorio o donde la puedas encontrar

### ✅ Paso 2: Copiar a la Carpeta Correcta
1. **Abre** la carpeta de tu proyecto: `ECOMMERCE_FERRETERIA`
2. **Ve a:** `static` → `img`
3. **Pega** tu archivo `banner-principal.jpg` ahí

**Ruta completa:** `ECOMMERCE_FERRETERIA/static/img/banner-principal.jpg`

### ✅ Paso 3: Activar el Banner
1. **Abre** el archivo: `templates/productos/home.html`
2. **Busca** la línea 9 que dice: `<div class="banner-fallback">`
3. **Agrega** `d-none` para que quede así:
   ```html
   <div class="banner-fallback d-none">
   ```
4. **Busca** las líneas 36-40 (el comentario)
5. **Descomenta** quitando `<!--` y `-->`

**Debe quedar así:**
```html
<div class="banner-image-container">
    <img src="{% static 'img/banner-principal.jpg' %}" alt="Ferretería Maipú - Banner Principal" class="img-fluid w-100" style="height: 400px; object-fit: cover;">
</div>
```

## 🔄 Ver el Resultado

1. **Guarda** los cambios
2. **Recarga** la página: http://127.0.0.1:8000/
3. **¡Tu banner aparecerá!** 🎉

## 🚨 Si No Funciona:

### Verifica:
- ✅ El archivo se llama exactamente: `banner-principal.jpg`
- ✅ Está en: `static/img/banner-principal.jpg`
- ✅ Descomentaste las líneas correctas
- ✅ Agregaste `d-none` al fallback

### Reinicia:
- Para el servidor: `Ctrl+C`
- Reinicia: `python manage.py runserver`

## 📐 Ajustar Tamaño (Opcional)

Si quieres cambiar la altura del banner:
- Busca: `height: 400px`
- Cámbialo por: `height: 300px` (o el tamaño que prefieras)

---

**¡En 5 minutos tendrás tu banner promocional funcionando!** 🎉🔧

**Estado Actual:** Tienes un hero section temporal con todos tus datos reales mientras agregas la imagen.