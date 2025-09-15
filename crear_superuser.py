#!/usr/bin/env python
import os
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ferreteria_ecommerce.settings')
django.setup()

from django.contrib.auth.models import User

# Crear superusuario
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@ferreteria.com', 'admin123')
    print("✅ Superusuario creado:")
    print("   Usuario: admin")
    print("   Email: admin@ferreteria.com")
    print("   Contraseña: admin123")
else:
    print("ℹ️ El superusuario 'admin' ya existe.")