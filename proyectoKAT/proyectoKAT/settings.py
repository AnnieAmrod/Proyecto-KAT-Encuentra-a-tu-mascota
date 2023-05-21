"""
Django settings for proyectoKAT project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os
from django.contrib.messages import constants as messages

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ifr62r-r-o)o!=5@c2p^6v8i!u3e)lz@j@cg^8levn4q)5c*br'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #Aplicación utilizada para administrar y gestionar sitios web, proporciona un modelo de base de datos para almacenar información sobre diferentes sitios web
    'django.contrib.sites',
    
    #Aplicaciones descargadas
    'ckeditor',
    'crispy_forms',
    'crispy_bootstrap5',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'django_filters',
    
    #Aplicaciones propias
    'common',
    'usuario',
    'katapp',
]

#Variable de configuración utilizada para especificar el ID del sitio que se está utilizando actualmente. Se utiliza en conjunción con la aplicación 'sites' de Django. Por defecto crea un registro, por ello lo igualamos a 1
SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'proyectoKAT.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                #Para que funcione allauth
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'proyectoKAT.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'katdb',
        'USER': 'miriam',
        'PASSWORD': 'miriamd',
        'HOST': 'localhost',
        'PORT': '3306',
        
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

#Configurar autenticación utilizando el modelo predeterminado de Django
AUTH_USER_MODEL = 'usuario.Usuario'

#Creamos las variables de configuración que indican la URL o vista a la que se redirigirá al usuario tras realizar login/logout
LOGIN_REDIRECT_URL = '/panel/'
LOGOUT_REDIRECT_URL = '/accounts/login/'

LOGIN_URL = '/login/'

#Se trata de una lista de clases de autenticación que se utilizan para autenticar a los usuarios. En este caso, django.contrib.auth.backends.ModelBackend nos proporciona una forma estándar de autenticar a los usuarios mediante el modelo User, mientras que allauth.account.auth_backends.AuthenticationBackend permite que el usuario inicie la sesión utilizando su dirección de correo electrónico y contraseña (Si no se encuentra en la primera clase de autenticación, se prueba en la siguiente clase sucesivamente hasta que encuentre una clase que autentique al usuario o hasta que no queden clases de autenticación, en este caso tenemos únicamente dos clases de autenticación)
AUTHENTICATION_BACKENDS = [
# Necesaria para realizar el login usando username en el administrador de Django, independiente de django allauth
    'django.contrib.auth.backends.ModelBackend',

    #métodos de autenticación especifica de  `allauth`, como por ejemplo email
    'allauth.account.auth_backends.AuthenticationBackend',
]

#Configuramos el sistema de gestión de usuarios para que requiera una dirección de correo electrónico para el registro y el inicio de sesión, en lugar de requerir un nombre de usuario. Utilizará el email como método de autenticación para el inicio de sesión
#La variable ACCOUNT_USER_MODEL_USERNAME_FIELD se utiliza para especificar el campo del modelo de usuario que se utilizará como nombre de usuario para iniciar sesión. Si se establece en None, indica que el sistema no utilizará un nombre de usuario para iniciar sesión
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
#La variable ACCOUNT_EMAIL_REQUIRED especifica si se requiere que los usuarios proporcionen una dirección de correo electrónico al registrarse en el sistema. Si se establece en True, indica que los usuarios deberán proporcionar una dirección de correo electrónico válida para poder registrarse
ACCOUNT_EMAIL_REQUIRED = True
#La variable ACCOUNT_USERNAME_REQUIRED especifica si se requiere que los usuarios proporcionen un nombre de usuario al registrarse en el sistema. Si se establece en False, significa que los usuarios no necesitan proporcionar un nombre de usuario para registrarse
ACCOUNT_USERNAME_REQUIRED = False
#La variable ACCOUNT_AUTHENTICATION_METHOD especifica el método de autenticación que se utilizará para iniciar sesión en el sistema. Si se establece en 'email', significa que los usuarios podrán iniciar sesión utilizando su dirección de correo electrónico en lugar de un nombre de usuario
ACCOUNT_AUTHENTICATION_METHOD = 'email'
#La variable ACCOUNT_EMAIL_VERIFICATION se utiliza para controlar cómo se verifican las direcciones de correo electrónico de los usuarios. Si se establece en 'mandatory', significa que se requiere que todos los usuarios verifiquen su dirección de correo antes de poder iniciar sesión o realizar acciones en la aplicación, se utiliza para evitar que los usuarios introduzcan direcciones de correo no válidas o falsas
#ACCOUNT_EMAIL_VERIFICATION = 'mandatory' #TODO descomentar cuando haga el tema de los emails

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'Europe/Madrid'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/


PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#Configuración CKEditor
#Información extraída de: github.com/django-ckeditor/django-ckeditor
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline'],
        ],
        'width': '235px',
        'height': '280px',
    }
}

MESSAGE_TAGS = {messages.ERROR: 'danger'}

#-------------------- Para que funcionen las plantillas de Crispy Forms
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"


CRISPY_TEMPLATE_PACK = "bootstrap5"