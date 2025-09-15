@echo off
title Comandos Rápidos - Ferretería E-commerce

echo.
echo ╔══════════════════════════════════════════════════════════════╗
echo ║                    COMANDOS RÁPIDOS                         ║
echo ║                 Ferretería E-commerce                       ║
echo ╚══════════════════════════════════════════════════════════════╝
echo.

:MENU
echo ┌─────────────────────────────────────────────────────────────┐
echo │                     OPCIONES DISPONIBLES                   │
echo ├─────────────────────────────────────────────────────────────┤
echo │  1. 🚀 Iniciar servidor                                    │
echo │  2. 🔍 Verificar estado del servidor                       │
echo │  3. 🗄️  Crear datos de ejemplo                             │
echo │  4. 👤 Crear superusuario                                  │
echo │  5. 🌐 Abrir página principal                              │
echo │  6. ⚙️  Abrir panel admin                                   │
echo │  7. 📋 Ver resumen del proyecto                            │
echo │  8. 🔧 Activar entorno virtual                             │
echo │  9. 📊 Ver estructura del proyecto                         │
echo │  0. Salir                                                  │
echo └─────────────────────────────────────────────────────────────┘
echo.

set /p "opcion=Seleccione una opción (0-9): "

if "%opcion%"=="1" goto INICIAR_SERVIDOR
if "%opcion%"=="2" goto VERIFICAR_SERVIDOR
if "%opcion%"=="3" goto CREAR_DATOS
if "%opcion%"=="4" goto CREAR_SUPERUSER
if "%opcion%"=="5" goto ABRIR_PAGINA
if "%opcion%"=="6" goto ABRIR_ADMIN
if "%opcion%"=="7" goto VER_RESUMEN
if "%opcion%"=="8" goto ACTIVAR_VENV
if "%opcion%"=="9" goto VER_ESTRUCTURA
if "%opcion%"=="0" goto SALIR

echo ❌ Opción inválida. Intente nuevamente.
echo.
pause
cls
goto MENU

:INICIAR_SERVIDOR
echo.
echo 🚀 Iniciando servidor Django...
call INICIAR_FERRETERIA.bat
goto MENU

:VERIFICAR_SERVIDOR
echo.
echo 🔍 Verificando estado del servidor...
call venv\Scripts\activate.bat
python verificar_servidor.py
echo.
pause
cls
goto MENU

:CREAR_DATOS
echo.
echo 🗄️ Creando datos de ejemplo...
call venv\Scripts\activate.bat
python crear_datos_ejemplo.py
echo.
pause
cls
goto MENU

:CREAR_SUPERUSER
echo.
echo 👤 Creando superusuario...
call venv\Scripts\activate.bat
python crear_superuser.py
echo.
pause
cls
goto MENU

:ABRIR_PAGINA
echo.
echo 🌐 Abriendo página principal...
start http://127.0.0.1:8000/
echo ✅ Página abierta en el navegador
echo.
pause
cls
goto MENU

:ABRIR_ADMIN
echo.
echo ⚙️ Abriendo panel de administración...
start http://127.0.0.1:8000/admin/
echo ✅ Panel admin abierto en el navegador
echo 👤 Usuario: admin
echo 🔑 Contraseña: admin123
echo.
pause
cls
goto MENU

:VER_RESUMEN
echo.
echo 📋 Abriendo resumen del proyecto...
start notepad RESUMEN_PROYECTO.md
echo.
pause
cls
goto MENU

:ACTIVAR_VENV
echo.
echo 🔧 Activando entorno virtual...
call venv\Scripts\activate.bat
echo ✅ Entorno virtual activado
echo 💡 Ahora puedes ejecutar comandos Django
echo.
pause
cls
goto MENU

:VER_ESTRUCTURA
echo.
echo 📊 Estructura del proyecto:
echo.
tree /F /A
echo.
pause
cls
goto MENU

:SALIR
echo.
echo 👋 ¡Hasta luego!
echo.
pause
exit