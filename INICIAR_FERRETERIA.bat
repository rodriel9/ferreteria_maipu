@echo off
title Ferretería E-commerce - Servidor Django

echo.
echo ╔══════════════════════════════════════════════════════════════╗
echo ║                    FERRETERÍA E-COMMERCE                     ║
echo ║                      Servidor Django                        ║
echo ╚══════════════════════════════════════════════════════════════╝
echo.

:: Cambiar al directorio del script
cd /d "%~dp0"

:: Verificar que existe el entorno virtual
if not exist "venv\Scripts\python.exe" (
    echo ❌ Error: No se encontró el entorno virtual
    echo 💡 Ejecuta primero: python -m venv venv
    pause
    exit /b 1
)

:: Verificar que existe manage.py
if not exist "manage.py" (
    echo ❌ Error: No se encontró manage.py
    echo 💡 Asegúrate de estar en el directorio correcto del proyecto
    pause
    exit /b 1
)

echo 🔄 Activando entorno virtual...
call venv\Scripts\activate.bat

echo 🔍 Verificando configuración Django...
venv\Scripts\python.exe manage.py check --deploy
if errorlevel 1 (
    echo ❌ Error en la configuración de Django
    pause
    exit /b 1
)

echo.
echo 🚀 Iniciando servidor Django...
echo.
echo ┌─────────────────────────────────────────────────────────────┐
echo │                     URLs DISPONIBLES                       │
echo ├─────────────────────────────────────────────────────────────┤
echo │  🏠 Página Principal: http://127.0.0.1:8000/              │
echo │  ⚙️  Panel Admin:      http://127.0.0.1:8000/admin/       │
echo │  📦 Catálogo:         http://127.0.0.1:8000/catalogo/     │
echo └─────────────────────────────────────────────────────────────┘
echo.
echo ┌─────────────────────────────────────────────────────────────┐
echo │                  CREDENCIALES ADMIN                        │
echo ├─────────────────────────────────────────────────────────────┤
echo │  👤 Usuario:   admin                                       │
echo │  🔑 Contraseña: admin123                                   │
echo └─────────────────────────────────────────────────────────────┘
echo.
echo ⚠️  Para detener el servidor presiona Ctrl+C
echo.

:: Abrir navegador automáticamente (opcional)
timeout /t 3 /nobreak >nul
start http://127.0.0.1:8000/

:: Iniciar servidor Django
venv\Scripts\python.exe manage.py runserver 127.0.0.1:8000

echo.
echo 👋 Servidor detenido.
pause