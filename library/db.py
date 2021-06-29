import json
import os

from django.core.exceptions import ImproperlyConfigured

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SQLITE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# psycopg2

POSTGRESQL = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'libreria_utp' ,
        'USER': 'postgres' ,
        'PASSWORD':'yamamoto7674',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}

# mysqlclient

MYSQL = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'mysqldb',
        'USER': 'juanel',
        'PASSWORD': '#Maremoto7674',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'sql_mode': 'traditional',
        }
    }
}
