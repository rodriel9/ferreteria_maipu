# 🖼️ Cómo Agregar el Logo de Ferretería Maipú

## 📋 Pasos para Integrar tu Logo

### 1. 📁 Preparar la Imagen
- **Formato recomendado:** PNG con fondo transparente
- **Tamaño:** 200x200 píxeles (o proporcional)
- **Nombre del archivo:** `logo-maipu.png`

### 2. 📂 Ubicar el Archivo
1. Abre la carpeta del proyecto: `ECOMMERCE_FERRETERIA`
2. Ve a la carpeta: `static/img/`
3. Copia tu logo con el nombre: `logo-maipu.png`

### 3. ✏️ Activar el Logo en el Navbar
Abre el archivo: `templates/base.html`

**Busca estas líneas (alrededor de la línea 87):**
```html
<!-- <img src="{% static 'img/logo-maipu.png' %}" alt="Ferretería Maipú" height="45" class="me-2"> -->

<!-- Placeholder mientras agregas tu logo -->
<div class="logo-placeholder d-inline-block">
    <i class="fas fa-tools text-danger"></i>
</div>
```

**Cámbialas por:**
```html
<img src="{% static 'img/logo-maipu.png' %}" alt="Ferretería Maipú" height="45" class="me-2">

<!-- Placeholder mientras agregas tu logo -->
<!-- <div class="logo-placeholder d-inline-block">
    <i class="fas fa-tools text-danger"></i>
</div> -->
```

### 4. 🏠 Agregar Logo Grande en la Página Principal (Opcional)
En el archivo: `templates/productos/home.html`

**Busca (línea 9):**
```html
<i class="fas fa-tools fa-4x text-white mb-3"></i>
```

**Cámbialo por:**
```html
<img src="{% static 'img/logo-maipu.png' %}" alt="Ferretería Maipú" style="height: 120px;" class="mb-3">
```

## 🔄 Reiniciar el Servidor

Después de hacer los cambios:
1. Para el servidor (Ctrl+C en la terminal)
2. Reinicia con: `python manage.py runserver`
3. Recarga la página: http://127.0.0.1:8000/

## 🎨 Personalización Adicional

### Ajustar Tamaño del Logo
- **Navbar:** Cambia `height="45"` por el valor que prefieras
- **Página principal:** Cambia `height: 120px` por el tamaño deseado

### Logo con Diferentes Tamaños
Puedes crear varios archivos:
- `logo-maipu-small.png` (para navbar)
- `logo-maipu-large.png` (para página principal)
- `logo-maipu-square.png` (para favicon)

## ✅ Verificar que Funciona

Después de agregar el logo:
1. ✅ Se ve en la barra de navegación superior
2. ✅ Se mantiene el texto "Ferretería Maipú"
3. ✅ Se ve la dirección "Av. Maipú 255"
4. ✅ El logo es clickeable (lleva al inicio)

## 🚨 Solución de Problemas

### El logo no aparece:
- Verifica que el archivo se llame exactamente: `logo-maipu.png`
- Verifica que esté en: `static/img/logo-maipu.png`
- Reinicia el servidor Django

### El logo se ve muy grande/pequeño:
- Ajusta el valor `height="45"` en el navbar
- Ajusta `height: 120px` en la página principal

### El logo se ve pixelado:
- Usa una imagen de mayor resolución
- Preferiblemente PNG con fondo transparente

## 📞 ¿Necesitas Ayuda?

Si tienes problemas para agregar el logo:
1. Verifica que el archivo esté en la ubicación correcta
2. Revisa que los cambios en HTML sean exactos
3. Reinicia el servidor Django
4. Limpia la caché del navegador (Ctrl+F5)

---

**¡Tu logo de Ferretería Maipú quedará perfecto!** 🎉