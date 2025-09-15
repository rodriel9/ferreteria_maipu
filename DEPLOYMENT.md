# 🚀 Deployment - E-commerce Ferretería

## 📋 Archivos de Deployment Creados

✅ **requirements.txt** - Dependencias de Python
✅ **Procfile** - Comando de inicio para Heroku/Railway
✅ **runtime.txt** - Versión de Python
✅ **railway.json** - Configuración para Railway
✅ **.gitignore** - Archivos a ignorar en Git
✅ **settings.py** - Configurado para producción

## 🌐 Opciones de Deployment

### 🚀 Opción 1: Railway (Recomendado)

1. **Ir a:** https://railway.app/
2. **Registrarse** con GitHub/Google
3. **Crear nuevo proyecto**
4. **Subir código:**
   - Conectar repositorio Git, O
   - Subir ZIP del proyecto
5. **Variables de entorno:**
   ```
   DEBUG=False
   SECRET_KEY=tu-clave-secreta-segura
   DATABASE_URL=(se configura automáticamente)
   ```
6. **Deploy automático** ✨

### ☁️ Opción 2: Render

1. **Ir a:** https://render.com/
2. **Conectar repositorio** o subir código
3. **Configurar como Web Service**
4. **Build Command:** `pip install -r requirements.txt`
5. **Start Command:** `gunicorn ferreteria_ecommerce.wsgi`
6. **Variables de entorno** (igual que Railway)

### 🐳 Opción 3: Heroku

```bash
# 1. Login a Heroku
heroku login

# 2. Crear app
heroku create tu-ferreteria-app

# 3. Configurar variables
heroku config:set DEBUG=False
heroku config:set SECRET_KEY=tu-clave-secreta

# 4. Deploy
git add .
git commit -m "Deploy to production"
git push heroku main

# 5. Migrar base de datos
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
```

## ⚙️ Variables de Entorno Necesarias

```env
DEBUG=False
SECRET_KEY=tu-clave-secreta-muy-segura-aqui
DATABASE_URL=postgres://... (se configura automáticamente)
```

## 🔧 Comandos Post-Deployment

Después del primer deployment:

```bash
# Migrar base de datos
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Cargar datos de ejemplo
python crear_datos_ejemplo.py
```

## 📱 URLs de Producción

- **Página principal:** https://tu-app.railway.app/
- **Admin:** https://tu-app.railway.app/admin/
- **Catálogo:** https://tu-app.railway.app/catalogo/

## 🔒 Seguridad en Producción

✅ DEBUG = False
✅ SECRET_KEY segura
✅ ALLOWED_HOSTS configurado
✅ WhiteNoise para archivos estáticos
✅ Base de datos PostgreSQL

## 💰 Costos Estimados

- **Railway:** $5/mes después de créditos gratis
- **Render:** $7/mes plan básico
- **Heroku:** $7/mes (sin plan gratuito)

## 🆘 Solución de Problemas

### Error de archivos estáticos:
```bash
python manage.py collectstatic --noinput
```

### Error de base de datos:
```bash
python manage.py migrate
```

### Error 500:
- Verificar variables de entorno
- Revisar logs del servidor
- Comprobar ALLOWED_HOSTS

## 🎉 ¡Tu E-commerce Estará Online!

Una vez deployado, tendrás:
- ✅ Página web accesible desde internet
- ✅ Base de datos en la nube
- ✅ Archivos estáticos servidos
- ✅ Panel de administración
- ✅ Carrito funcional
- ✅ Catálogo completo