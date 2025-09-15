#!/usr/bin/env python3
"""
Script para verificar si el servidor Django está funcionando
"""

import requests
import sys
import time

def verificar_servidor():
    url = "http://127.0.0.1:8000/"
    
    print("🔍 Verificando servidor Django...")
    print(f"📍 URL: {url}")
    
    try:
        response = requests.get(url, timeout=5)
        
        if response.status_code == 200:
            print("✅ ¡Servidor funcionando correctamente!")
            print(f"📊 Código de respuesta: {response.status_code}")
            print(f"🌐 Página disponible en: {url}")
            print(f"⚙️ Panel admin en: http://127.0.0.1:8000/admin/")
            print("\n👤 Credenciales de admin:")
            print("   Usuario: admin")
            print("   Contraseña: admin123")
            return True
        else:
            print(f"⚠️ Servidor responde pero con error: {response.status_code}")
            return False
            
    except requests.exceptions.ConnectionError:
        print("❌ No se puede conectar al servidor")
        print("💡 Soluciones:")
        print("   1. Ejecutar: python manage.py runserver")
        print("   2. O ejecutar: iniciar_servidor.bat")
        print("   3. Verificar que no haya errores en Django")
        return False
        
    except requests.exceptions.Timeout:
        print("⏰ Timeout - El servidor tarda en responder")
        return False
        
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
        return False

if __name__ == "__main__":
    if verificar_servidor():
        print("\n🚀 ¡Todo listo para usar la ferretería online!")
    else:
        print("\n🔧 Necesitas iniciar el servidor primero.")
        sys.exit(1)