import os
import dj_database_url
from .settings import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Hosts permitidos
ALLOWED_HOSTS = [
    'tu-ferreteria.herokuapp.com',  # Cambiar por tu dominio de Heroku
    '127.0.0.1',
    'localhost',
    '.railway.app', # Añadido .railway.app para compatibilidad con Railway
    '.render.com',  # Añadido .render.com para compatibilidad con Render
]

# Base de datos para producción (PostgreSQL en Heroku/Railway/Render)
DATABASES = {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
}

# Configuración de archivos estáticos para producción
# STATIC_URL y STATIC_ROOT ya están definidos en settings.py y son manejados por WhiteNoise
# STATICFILES_DIRS y STATICFILES_STORAGE también están en settings.py
# Ya no necesitamos duplicarlos aquí.

# Middleware con WhiteNoise - ya está en settings.py con whitenoise.middleware.WhiteNoiseMiddleware
# MIDDLEWARE = [
#    'django.middleware.security.SecurityMiddleware',
#    'whitenoise.middleware.WhiteNoiseMiddleware',  # WhiteNoise
#    'django.contrib.sessions.middleware.SessionMiddleware',
#    'django.middleware.common.CommonMiddleware',
#    'django.middleware.csrf.CsrfViewMiddleware',
#    'django.contrib.auth.middleware.AuthenticationMiddleware',
#    'django.contrib.messages.middleware.MessageMiddleware',
#    'django.middleware.clickjacking.XFrameOptionsMiddleware',
# ]

# Configuración de archivos media (imágenes) - ya está en settings.py
# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Configuración de seguridad para producción
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

# Variables de entorno
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-cambiar-en-produccion')

# Email configuration (opcional)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ.get('EMAIL_HOST', 'smtp.gmail.com')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')

# Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'django.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}