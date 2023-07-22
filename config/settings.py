"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os.path
import sys
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-3hot3eg$sr1avw4o6avilt+&bz@qve)+oklbgp)70dkmz3-xdv"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS: list[str] = []

# Include BOOTSTRAP4_FOLDER in path
BOOTSTRAP4_FOLDER = os.path.abspath(os.path.join(BASE_DIR, "..", "bootstrap4"))
if BOOTSTRAP4_FOLDER not in sys.path:
    sys.path.insert(0, BOOTSTRAP4_FOLDER)

# GDAL-GEOS_PATH
GDAL_LIBRARY_PATH = os.environ.get("GDAL_LIBRARY_PATH")
GEOS_LIBRARY_PATH = os.environ.get("GEOS_LIBRARY_PATH")

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.gis",
    "apps.core.apps.CoreConfig",
    "apps.events.apps.EventsConfig",
    "apps.permissions.apps.PermissionsConfig",
    "location_field.apps.DefaultConfig",
    "widget_tweaks",
    "bootstrap4",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
            ]
        },
    }
]

WSGI_APPLICATION = "config.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": BASE_DIR / "db.sqlite3"}}
DATABASES = {
    "default": {
        "ENGINE": "django.contrib.gis.db.backends.postgis",
        "NAME": os.getenv("POSTGRES_DB"),
        "USER": os.getenv("POSTGRES_USER"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD"),
        "HOST": os.getenv("DB_HOST", "localhost"),
        "PORT": os.getenv("DB_PORT", "5555"),
    }
}
# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

password_validation = "django.contrib.auth.password_validation"
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": f"{password_validation}.UserAttributeSimilarityValidator"},
    {"NAME": f"{password_validation}.MinimumLengthValidator"},
    {"NAME": f"{password_validation}.CommonPasswordValidator"},
    {"NAME": f"{password_validation}.NumericPasswordValidator"},
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "/static/"
STATICFILES_DIRS = (BASE_DIR / "static",)

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)

# Settings for django-bootstrap4
BOOTSTRAP4 = {
    "error_css_class": "bootstrap4-error",
    "required_css_class": "bootstrap4-required",
    "javascript_in_head": True,
    "include_jquery": True,
}

LOCATION_FIELD_PATH = STATIC_URL + "location_field"

LOCATION_FIELD = {
    "map.provider": "google",
    "map.zoom": 13,
    "search.provider": "yandex",
    "search.suffix": "",
    # Yandex
    "provider.yandex.api_key": os.getenv("YANDEX_MAPS_API_KEY"),
    # Google
    "provider.google.api": "//maps.google.com/maps/api/js",
    "provider.google.api_key": os.getenv("GOOGLE_MAPS_API_KEY"),
    "provider.google.map_type": "ROADMAP",
    # Mapbox
    "provider.mapbox.access_token": "",
    "provider.mapbox.max_zoom": 18,
    "provider.mapbox.id": "mapbox.streets",
    # OpenStreetMap
    "provider.openstreetmap.max_zoom": 18,
    # misc
    "resources.root_path": LOCATION_FIELD_PATH,
    "resources.media": {"js": [LOCATION_FIELD_PATH + "/js/form.js"]},
}
