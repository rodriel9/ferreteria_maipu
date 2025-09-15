# 🚀 Cómo Iniciar el Servidor de la Ferretería E-commerce

## 📋 Pasos para Iniciar el Servidor:

### **Opción 1: Usar el Script Automático**
1. Hacer doble clic en: `iniciar_servidor.bat`
2. El script se encargará de todo automáticamente

### **Opción 2: Línea de Comandos Manual**
```powershell
# 1. Abrir PowerShell en el directorio del proyecto
cd F:\pruebaG\nueva_forma\ECOMMERCE_FERRETERIA

# 2. Activar el entorno virtual
.\venv\Scripts\Activate.ps1

# 3. Iniciar el servidor
.\venv\Scripts\python.exe manage.py runserver
```

### **Opción 3: Usando Python Directo**
```powershell
# En el directorio del proyecto:
.\venv\Scripts\python.exe manage.py runserver 127.0.0.1:8000
```

## 🌐 URLs una vez que el servidor esté corriendo:

- **🏠 Página Principal:** http://127.0.0.1:8000/
- **⚙️ Panel Admin:** http://127.0.0.1:8000/admin/
- **📦 Catálogo:** http://127.0.0.1:8000/catalogo/

## 👤 Credenciales de Admin:
- **Usuario:** `admin`
- **Contraseña:** `admin123`

## 🔧 Solución de Problemas:

### Si el servidor no inicia:
1. Verificar que estés en el directorio correcto
2. Activar el entorno virtual correctamente
3. Usar la ruta completa de Python: `.\venv\Scripts\python.exe`

### Si la página no carga:
1. Verificar que el servidor esté corriendo (debe mostrar mensajes en la consola)
2. Verificar la URL: http://127.0.0.1:8000/
3. Ejecutar: `python verificar_servidor.py` para diagnóstico

## ✅ Señales de que el Servidor está Funcionando:
- Verás mensajes como: "Starting development server at http://127.0.0.1:8000/"
- La consola mostrará peticiones HTTP cuando navegues
- El script `verificar_servidor.py` mostrará "✅ Servidor funcionando correctamente!"

## 🎯 Demo Completamente Funcional:
Una vez iniciado el servidor, tendrás acceso a:
- ✅ **10 productos** de ferretería precargados
- ✅ **8 categorías** completas
- ✅ **Panel administrativo** completo
- ✅ **Diseño responsivo** profesional
- ✅ **Búsqueda** de productos
- ✅ **Sistema de ofertas** y descuentos