@echo off
echo.
echo ╔══════════════════════════════════════════════════════════════╗
echo ║                    FERRETERÍA E-COMMERCE                     ║
echo ║                   Iniciando Servidor...                     ║
echo ╚══════════════════════════════════════════════════════════════╝
echo.

cd /d "%~dp0"
call venv\Scripts\activate.bat

echo 🚀 Iniciando servidor Django...
echo.
echo 📍 URLs disponibles:
echo    🏠 Página Principal: http://127.0.0.1:8000/
echo    ⚙️  Panel Admin:      http://127.0.0.1:8000/admin/
echo.
echo 👤 Credenciales Admin:
echo    Usuario: admin
echo    Contraseña: admin123
echo.
echo ⚠️  Para detener el servidor presiona Ctrl+C
echo.

venv\Scripts\python.exe manage.py runserver

pause