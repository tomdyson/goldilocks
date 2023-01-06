import os
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration


PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)

env = os.environ.copy()

running_on_fly = False
if os.environ.get("FLY_APP_NAME"):
    running_on_fly = True

if "SENTRY_DSN" in env:
    sentry_sdk.init(
        dsn=os.environ["SENTRY_DSN"],
        integrations=[DjangoIntegration()],
        traces_sample_rate=1.0,
    )

if "SECRET_KEY" in env:
    SECRET_KEY = env["SECRET_KEY"]

ALLOWED_HOSTS = [
    "goldilocks.fly.dev",
    "goldilocksrecords.com",
    "www.goldilocksrecords.com",
]

CSRF_TRUSTED_ORIGINS = ["https://goldilocks.fly.dev", "https://goldilocksrecords.com"]

if "ALLOWED_HOSTS" in env:
    ALLOWED_HOSTS = env["ALLOWED_HOSTS"].split(",")

INSTALLED_APPS = [
    "home",
    "blog",
    "corsheaders",
    "search",
    "rest_framework",
    "wagtail.api.v2",
    "wagtail.contrib.forms",
    "wagtail.contrib.modeladmin",
    "wagtail.contrib.redirects",
    "wagtail.contrib.settings",
    "wagtail.embeds",
    "wagtail.sites",
    "wagtail.users",
    "wagtail.snippets",
    "wagtail.documents",
    "wagtail.images",
    "wagtail.search",
    "wagtail.admin",
    "wagtail.core",
    "modelcluster",
    "taggit",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "wagtailmedia",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "wagtail.contrib.redirects.middleware.RedirectMiddleware",
]

ROOT_URLCONF = "tomd.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(PROJECT_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "wagtail.contrib.settings.context_processors.settings",
            ]
        },
    }
]

WSGI_APPLICATION = "tomd.wsgi.application"

if running_on_fly:
    SQLITE_PATH = "/data/goldilocks.sqlite3"
else:
    SQLITE_PATH = os.path.join(BASE_DIR, "goldilocks.sqlite3")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": SQLITE_PATH,
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LANGUAGE_CODE = "en-gb"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]
STATICFILES_DIRS = [os.path.join(PROJECT_DIR, "static")]
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = "/static/"

MEDIA_URL = "/media/"
if running_on_fly:
    MEDIA_ROOT = "/data/media"
else:
    MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Wagtail settings
WAGTAIL_SITE_NAME = "Goldilocks"

# Base URL to use when referring to full URLs within the Wagtail admin backend,
# e.g. in notification emails.
BASE_URL = "https://calais2021.tomd.org"

CORS_ORIGIN_ALLOW_ALL = True
WAGTAILEMBEDS_RESPONSIVE_HTML = True

WAGTAILADMIN_BASE_URL = "http://example.com"
DEFAULT_AUTO_FIELD = "django.db.models.AutoField"
