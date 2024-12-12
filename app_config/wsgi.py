"""
This file contains all necessary configurations for wsgi deployment support
"""

import os
from django.core.wsgi import get_wsgi_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE','app_config.settings')
application= get_wsgi_application()