"""
This file contains all configurations to manage the project and deploy the server.
Don't forget to make this executable on your command line with the command: 'chmod +x manage.py'
"""

import os
import sys

if __name__=='__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app_config.settings')

    try:
        from django.core.management import execute_from_command_line

    except ImportError as exc:
        raise ImportError(
            'Could not import Django. Are you sure it is installed and available'
            'on your PYTHON PATH environment variable? Or maybe you'
            'forgot to activate a virtual environment?'
        )

    execute_from_command_line(sys.argv)