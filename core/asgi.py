"""
ASGI config for core project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os
from core.settings.environment import APPLICATION_ENVIRONMENT

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'core.settings.{APPLICATION_ENVIRONMENT}')

application = get_asgi_application()
