"""
This file contains necessary configuration settings for the application
"""

import os
from mongoengine import connect
from dotenv import load_dotenv

load_dotenv()

BASE_DIR= os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY= os.getenv('SECRET_KEY') #from .env file
DEBUG= True

ALLOWED_HOSTS=['127.0.0.1']
INSTALLED_APPS=[]
MIDDLEWARE= [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
]
ROOT_URLCONF= 'app_config.urls'
WSGI_APPLICATION= 'app_config.wsgi.application'
ASGI_APPLICATION= 'app_config.asgi.application'
DATABASES= {
    'default':{
        'ENGINE':'django.db.backends.postgresql',
        'NAME':'erp_management_database',
        'USER':'project_tester',
        'PASSWORD':'dedsec',
        'HOST':'localhost',
        'PORT':5432,
    }
}

connect(
db='mongo_erp_management_database',
host = 'mongodb://project_tester:dedsec@localhost:27017/mongo_erp_management_database',
port = 27017
)

LANGUAGE_CODE='en-us'
TIME_ZONE='UTC'
USE_LI0N=True
USE_I10N=True
USE_TZ=True
STATIC_URL='/static/'

LOGGING= {
    'version': 1,
    'disable_existing_loggers':False,
    'handlers': {
        'file': {
            'level':'ERROR',
            'class':'logging.FileHandler',
            'filename':'logs/errors.log', # ensure logs directory exists
        },
    },

    'loggers':{
        'django':{
            'handlers': ['file'],
            'level':'ERROR',
            'propagate':True,
        },
    },
}