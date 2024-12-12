"""
This file contains all necessary configurations for asgi deployment support
"""

import os
from django.core.asgi import get_asgi_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE','app_config.settings')
application= get_asgi_application()