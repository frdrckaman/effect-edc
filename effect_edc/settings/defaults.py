import os
import sys
from pathlib import Path

import environ
from edc_appointment.constants import SCHEDULED_APPT, UNSCHEDULED_APPT
from edc_constants.constants import COMPLETE
from edc_utils import get_datetime_from_env

BASE_DIR = str(Path(os.path.dirname(os.path.abspath(__file__))).parent.parent)
ENV_DIR = str(Path(os.path.dirname(os.path.abspath(__file__))).parent.parent)
env = environ.Env(
    AWS_ENABLED=(bool, False),
    CDN_ENABLED=(bool, False),
    CELERY_ENABLED=(bool, False),
    DATABASE_SQLITE_ENABLED=(bool, False),
    DJANGO_AUTO_CREATE_KEYS=(bool, False),
    DJANGO_CRYPTO_FIELDS_TEMP_PATH=(bool, False),
    DJANGO_CSRF_COOKIE_SECURE=(bool, True),
    DJANGO_DEBUG=(bool, False),
    DJANGO_EDC_BOOTSTRAP=(int, 3),
    DJANGO_EMAIL_ENABLED=(bool, False),
    DJANGO_EMAIL_USE_TLS=(bool, True),
    DJANGO_LIVE_SYSTEM=(bool, False),
    DJANGO_LOGGING_ENABLED=(bool, True),
    DJANGO_SESSION_COOKIE_SECURE=(bool, True),
    DJANGO_USE_I18N=(bool, True),
    DJANGO_USE_L10N=(bool, False),
    DJANGO_USE_TZ=(bool, True),
    DEFENDER_ENABLED=(bool, False),
    EDC_RANDOMIZATION_REGISTER_DEFAULT_RANDOMIZER=(bool, True),
    EDC_LABEL_BROWSER_PRINT_PAGE_AUTO_BACK=(bool, True),
    SAUCE_ENABLED=(bool, False),
    SENTRY_ENABLED=(bool, False),
    SIMPLE_HISTORY_PERMISSIONS_ENABLED=(bool, False),
    SIMPLE_HISTORY_REVERT_DISABLED=(bool, False),
    TWILIO_ENABLED=(bool, False),
)

# copy your .env file from .envs/ to BASE_DIR
if "test" in sys.argv:
    env.read_env(os.path.join(ENV_DIR, ".env-tests"))
    print(f"Reading env from {os.path.join(BASE_DIR, '.env-tests')}")
else:
    if not os.path.exists(os.path.join(ENV_DIR, ".env")):
        raise FileExistsError(
            f"Environment file does not exist. Got `{os.path.join(ENV_DIR, '.env')}`"
        )
    env.read_env(os.path.join(ENV_DIR, ".env"))

DEBUG = env("DJANGO_DEBUG")

SECRET_KEY = env.str("DJANGO_SECRET_KEY")

APP_NAME = env.str("DJANGO_APP_NAME")

LIVE_SYSTEM = env.str("DJANGO_LIVE_SYSTEM")

ETC_DIR = env.str("DJANGO_ETC_FOLDER")

TEST_DIR = os.path.join(BASE_DIR, APP_NAME, "tests")

ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS")

ENFORCE_RELATED_ACTION_ITEM_EXISTS = False

DEFAULT_APPOINTMENT_TYPE = "hospital"

# LOGIN_REDIRECT_URL = env.str("DJANGO_LOGIN_REDIRECT_URL")
LOGIN_URL = "/accounts/login/"
LOGOUT_REDIRECT_URL = "/accounts/login/"

SENTRY_ENABLED = env("SENTRY_ENABLED")
DEFENDER_ENABLED = env("DEFENDER_ENABLED")

INSTALLED_APPS = [
    # "django.contrib.admin",
    "effect_edc.apps.AdminConfig",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "defender",
    "multisite",
    "django_crypto_fields.apps.AppConfig",
    "django_revision.apps.AppConfig",
    "django_extensions",
    "django_celery_results",
    "django_celery_beat",
    "logentry_admin",
    "simple_history",
    "storages",
    "edc_action_item.apps.AppConfig",
    "edc_appointment.apps.AppConfig",
    "edc_adverse_event.apps.AppConfig",
    "edc_consent.apps.AppConfig",
    "edc_crf.apps.AppConfig",
    "edc_csf.apps.AppConfig",
    "edc_reportable.apps.AppConfig",
    "edc_lab.apps.AppConfig",
    "edc_visit_schedule.apps.AppConfig",
    "edc_visit_tracking.apps.AppConfig",
    "edc_device.apps.AppConfig",
    "edc_dashboard.apps.AppConfig",
    "edc_data_manager.apps.AppConfig",
    "edc_document_status.apps.AppConfig",
    "edc_export.apps.AppConfig",
    "edc_facility.apps.AppConfig",
    "edc_fieldsets.apps.AppConfig",
    "edc_form_validators.apps.AppConfig",
    "edc_lab_dashboard.apps.AppConfig",
    "edc_label.apps.AppConfig",
    "edc_list_data.apps.AppConfig",
    "edc_identifier.apps.AppConfig",
    "edc_locator.apps.AppConfig",
    "edc_metadata.apps.AppConfig",
    "edc_microbiology.apps.AppConfig",
    "edc_model.apps.AppConfig",
    "edc_model_fields.apps.AppConfig",
    "edc_model_admin.apps.AppConfig",
    "edc_navbar.apps.AppConfig",
    "edc_notification.apps.AppConfig",
    "edc_offstudy.apps.AppConfig",
    "edc_pharmacy.apps.AppConfig",
    "edc_pdutils.apps.AppConfig",
    "edc_protocol.apps.AppConfig",
    "edc_protocol_violation.apps.AppConfig",
    "edc_prn.apps.AppConfig",
    "edc_randomization.apps.AppConfig",
    "edc_reference.apps.AppConfig",
    "edc_registration.apps.AppConfig",
    "edc_pdf_reports.apps.AppConfig",
    "edc_review_dashboard.apps.AppConfig",
    "edc_screening.apps.AppConfig",
    "edc_sites.apps.AppConfig",
    "edc_subject_dashboard.apps.AppConfig",
    "edc_timepoint.apps.AppConfig",
    "edc_unblinding.apps.AppConfig",
    "edc_form_describer.apps.AppConfig",
    "edc_adherence.apps.AppConfig",
    "edc_dx.apps.AppConfig",
    "edc_refusal.apps.AppConfig",
]
EFFECT_APPS = [
    "effect_consent.apps.AppConfig",
    "effect_lists.apps.AppConfig",
    "effect_dashboard.apps.AppConfig",
    "effect_labs.apps.AppConfig",
    # "effect_metadata_rules.apps.AppConfig",
    "effect_subject.apps.AppConfig",
    "effect_visit_schedule.apps.AppConfig",
    "effect_ae.apps.AppConfig",
    "effect_auth.apps.AppConfig",
    "effect_prn.apps.AppConfig",
    "effect_export.apps.AppConfig",
    "effect_screening.apps.AppConfig",
    "effect_sites.apps.AppConfig",
    "effect_edc.apps.AppConfig",
]
INSTALLED_APPS.extend(EFFECT_APPS)
INSTALLED_APPS.append("edc_auth.apps.AppConfig")

if not DEFENDER_ENABLED:
    INSTALLED_APPS.pop(INSTALLED_APPS.index("defender"))
# if env("SENTRY_ENABLED"):
#     INSTALLED_APPS.append("raven.contrib.django.raven_compat")

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "multisite.middleware.DynamicSiteMiddleware",
    "django.contrib.sites.middleware.CurrentSiteMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "defender.middleware.FailedLoginMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

if not DEFENDER_ENABLED:
    MIDDLEWARE.pop(MIDDLEWARE.index("defender.middleware.FailedLoginMiddleware"))

MIDDLEWARE.extend(
    [
        "edc_dashboard.middleware.DashboardMiddleware",
        "edc_subject_dashboard.middleware.DashboardMiddleware",
        "edc_lab_dashboard.middleware.DashboardMiddleware",
        "edc_adverse_event.middleware.DashboardMiddleware",
        # 'simple_history.middleware.HistoryRequestMiddleware'
    ]
)

ROOT_URLCONF = f"{APP_NAME}.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

if env("DATABASE_SQLITE_ENABLED"):
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        }
    }

else:
    DATABASES = {"default": env.db()}
# be secure and clear DATABASE_URL since it is no longer needed.
DATABASE_URL = None

if env.str("DJANGO_CACHE") == "redis":
    CACHES = {
        "default": {
            "BACKEND": "django_redis.cache.RedisCache",
            "LOCATION": "redis://127.0.0.1:6379/1",
            # "LOCATION": "unix://[:{DJANGO_REDIS_PASSWORD}]@/path/to/socket.sock?db=0",
            "OPTIONS": {
                "CLIENT_CLASS": "django_redis.client.DefaultClient",
                "PASSWORD": env.str("DJANGO_REDIS_PASSWORD"),
            },
            "KEY_PREFIX": f"{APP_NAME}",
        }
    }
    SESSION_ENGINE = "django.contrib.sessions.backends.cache"
    SESSION_CACHE_ALIAS = "default"
    DJANGO_REDIS_IGNORE_EXCEPTIONS = True
    DJANGO_REDIS_LOG_IGNORED_EXCEPTIONS = True

elif env.str("DJANGO_CACHE") == "memcached":
    CACHES = {
        "default": {
            "BACKEND": "django.core.cache.backends.memcached.PyLibMCCache",
            "LOCATION": "unix:/tmp/memcached.sock",
        }
    }
    SESSION_ENGINE = "django.contrib.sessions.backends.cached_db"

WSGI_APPLICATION = f"{APP_NAME}.wsgi.application"

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTHENTICATION_BACKENDS = ["edc_auth.backends.ModelBackendWithSite"]

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        "OPTIONS": {"min_length": 20},
    },
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]
# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = env.str("DJANGO_LANGUAGE_CODE")
# LANGUAGES = [x.split(":") for x in env.list("DJANGO_LANGUAGES")] or (("en", "English"),)
LANGUAGES = [
    ("en", "English"),
    ("af", "Afrikaans"),
    ("st", "Sotho"),
    ("sw", "Swahili"),
    ("tn", "Tswana"),
    ("xh", "Xhosa"),
    ("zu", "Zulu"),
]


TIME_ZONE = env.str("DJANGO_TIME_ZONE")

USE_I18N = env("DJANGO_USE_I18N")

# set to False so DATE formats below are used
USE_L10N = env("DJANGO_USE_L10N")

USE_TZ = env("DJANGO_USE_TZ")

DATE_INPUT_FORMATS = ["%Y-%m-%d", "%d/%m/%Y"]
DATETIME_INPUT_FORMATS = [
    "%Y-%m-%d %H:%M:%S",  # '2006-10-25 14:30:59'
    "%Y-%m-%d %H:%M:%S.%f",  # '2006-10-25 14:30:59.000200'
    "%Y-%m-%d %H:%M",  # '2006-10-25 14:30'
    "%Y-%m-%d",  # '2006-10-25'
    "%d/%m/%Y %H:%M:%S",  # '25/10/2006 14:30:59'
    "%d/%m/%Y %H:%M:%S.%f",  # '25/10/2006 14:30:59.000200'
    "%d/%m/%Y %H:%M",  # '25/10/2006 14:30'
    "%d/%m/%Y",  # '25/10/2006'
]
DATE_FORMAT = "j N Y"
DATETIME_FORMAT = "j N Y H:i"
SHORT_DATE_FORMAT = "d/m/Y"
SHORT_DATETIME_FORMAT = "d/m/Y H:i"

# See also any inte_* or edc_* apps.py
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# edc-pdutils
EXPORT_FILENAME_TIMESTAMP_FORMAT = "%Y%m%d"

# django_revision
with open(os.path.join(os.path.dirname(os.path.join(BASE_DIR, APP_NAME)), "VERSION")) as f:
    REVISION = f.read().strip()

# EDC_AUTH_SKIP_AUTH_UPDATER = True

# enforce https if DEBUG=False!
# Note: will cause "CSRF verification failed. Request aborted"
#       if DEBUG=False and https not configured.
if not DEBUG:
    # CSFR cookies
    CSRF_COOKIE_SECURE = env.str("DJANGO_CSRF_COOKIE_SECURE")
    SECURE_PROXY_SSL_HEADER = env.tuple("DJANGO_SECURE_PROXY_SSL_HEADER")
    SESSION_COOKIE_SECURE = env.str("DJANGO_SESSION_COOKIE_SECURE")

    # other security defaults
    SECURE_SSL_REDIRECT = True
    SECURE_HSTS_SECONDS = 31_536_000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_BROWSER_XSS_FILTER = True

# edc_lab and label
LABEL_TEMPLATE_FOLDER = env.str("DJANGO_LABEL_TEMPLATE_FOLDER") or os.path.join(
    BASE_DIR, "label_templates", "2.25x1.25in"
)
CUPS_SERVERS = env.dict("DJANGO_CUPS_SERVERS")

LIST_MODEL_APP_LABEL = env.str("EDC_LIST_MODEL_APP_LABEL")
SUBJECT_APP_LABEL = env.str("EDC_SUBJECT_APP_LABEL")
SUBJECT_SCREENING_MODEL = env.str("EDC_SUBJECT_SCREENING_MODEL")
SUBJECT_CONSENT_MODEL = env.str("EDC_SUBJECT_CONSENT_MODEL")
SUBJECT_REQUISITION_MODEL = env.str("EDC_SUBJECT_REQUISITION_MODEL")
SUBJECT_VISIT_MODEL = env.str("EDC_SUBJECT_VISIT_MODEL")
SUBJECT_VISIT_MISSED_MODEL = env.str("EDC_SUBJECT_VISIT_MISSED_MODEL")
SUBJECT_VISIT_MISSED_REASONS_MODEL = env.str("EDC_SUBJECT_VISIT_MISSED_REASONS_MODEL")

EDC_BLOOD_RESULTS_MODEL_APP_LABEL = "effect_subject"
EDC_DASHBOARD_APP_LABEL = "effect_dashboard"
EDC_NAVBAR_DEFAULT = env("EDC_NAVBAR_DEFAULT")

# dashboards
EDC_BOOTSTRAP = env("DJANGO_EDC_BOOTSTRAP")
DASHBOARD_URL_NAMES = env.dict("DJANGO_DASHBOARD_URL_NAMES")
DASHBOARD_BASE_TEMPLATES = env.dict("DJANGO_DASHBOARD_BASE_TEMPLATES")
LAB_DASHBOARD_BASE_TEMPLATES = env.dict("DJANGO_LAB_DASHBOARD_BASE_TEMPLATES")
LAB_DASHBOARD_URL_NAMES = env.dict("DJANGO_LAB_DASHBOARD_URL_NAMES")

# edc-diagnosis
EDC_DX_LABELS = dict(hiv="HIV", dm="Diabetes", htn="Hypertension", chol="High Cholesterol")
# edc-label
EDC_LABEL_BROWSER_PRINT_PAGE_AUTO_BACK = env("EDC_LABEL_BROWSER_PRINT_PAGE_AUTO_BACK")

# edc_facility
HOLIDAY_FILE = env.str("DJANGO_HOLIDAY_FILE")
EDC_FACILITY_USE_DEFAULTS = True

# edc_randomization
EDC_RANDOMIZATION_LIST_PATH = env.str("EDC_RANDOMIZATION_LIST_PATH")
EDC_RANDOMIZATION_UNBLINDED_USERS = env.list("EDC_RANDOMIZATION_UNBLINDED_USERS")
EDC_RANDOMIZATION_REGISTER_DEFAULT_RANDOMIZER = env(
    "EDC_RANDOMIZATION_REGISTER_DEFAULT_RANDOMIZER"
)
EDC_RANDOMIZATION_SKIP_VERIFY_CHECKS = True
EDC_RANDOMIZATION_ASSIGNMENT_MAP = env.dict("EDC_RANDOMIZATION_ASSIGNMENT_MAP")
# edc-sites
EDC_SITES_MODULE_NAME = env.str("EDC_SITES_MODULE_NAME")

# django-simple-history
SIMPLE_HISTORY_REVERT_ENABLED = False

# django-multisite
CACHE_MULTISITE_KEY_PREFIX = APP_NAME
SILENCED_SYSTEM_CHECKS = ["sites.E101"]

# django-defender
# see if env.str("DJANGO_CACHE") == "redis" above
# and that redis server is running
DEFENDER_REDIS_NAME = "default"
DEFENDER_LOCK_OUT_BY_IP_AND_USERNAME = True
DEFENDER_LOCKOUT_TEMPLATE = "edc_auth/bootstrap3/login.html"
DEFENDER_LOGIN_FAILURE_LIMIT = 5

# edc_crf
CRF_STATUS_DEFAULT = COMPLETE

EMAIL_ENABLED = env("DJANGO_EMAIL_ENABLED")
EMAIL_CONTACTS = env.dict("DJANGO_EMAIL_CONTACTS")
if EMAIL_ENABLED:
    EMAIL_HOST = env.str("DJANGO_EMAIL_HOST")
    EMAIL_PORT = env.int("DJANGO_EMAIL_PORT")
    EMAIL_HOST_USER = env.str("DJANGO_EMAIL_HOST_USER")
    EMAIL_HOST_PASSWORD = env.str("DJANGO_EMAIL_HOST_PASSWORD")
    EMAIL_USE_TLS = env("DJANGO_EMAIL_USE_TLS")
    MAILGUN_API_KEY = env("MAILGUN_API_KEY")
    MAILGUN_API_URL = env("MAILGUN_API_URL")

TWILIO_ENABLED = False  # env("TWILIO_ENABLED")
if TWILIO_ENABLED:
    TWILIO_ACCOUNT_SID = env.str("TWILIO_ACCOUNT_SID")
    TWILIO_AUTH_TOKEN = env.str("TWILIO_AUTH_TOKEN")
    TWILIO_SENDER = env.str("TWILIO_SENDER")

# django_revision
GIT_DIR = BASE_DIR

# django_crypto_fields
KEY_PATH = env.str("DJANGO_KEY_FOLDER")
AUTO_CREATE_KEYS = env.str("DJANGO_AUTO_CREATE_KEYS")

EXPORT_FOLDER = env.str("DJANGO_EXPORT_FOLDER") or os.path.expanduser("~/")

# django_simple_history
SIMPLE_HISTORY_PERMISSIONS_ENABLED = env.str("SIMPLE_HISTORY_PERMISSIONS_ENABLED")
SIMPLE_HISTORY_REVERT_DISABLED = env.str("SIMPLE_HISTORY_REVERT_DISABLED")

FQDN = env.str("DJANGO_FQDN")  # ???
INDEX_PAGE = env.str("DJANGO_INDEX_PAGE")
INDEX_PAGE_LABEL = env.str("DJANGO_INDEX_PAGE_LABEL")
DJANGO_LOG_FOLDER = env.str("DJANGO_LOG_FOLDER")

# edc_adverse_event
ADVERSE_EVENT_ADMIN_SITE = env.str("EDC_ADVERSE_EVENT_ADMIN_SITE")
ADVERSE_EVENT_APP_LABEL = env.str("EDC_ADVERSE_EVENT_APP_LABEL")

# edc_data_manager
DATA_DICTIONARY_APP_LABELS = [
    "effect_consent",
    "effect_subject",
    "effect_prn",
    "effect_screening",
    "effect_ae",
    "edc_appointment",
]

# edc_protocol
EDC_PROTOCOL = env.str("EDC_PROTOCOL")
EDC_PROTOCOL_INSTITUTION_NAME = env.str("EDC_PROTOCOL_INSTITUTION_NAME")
EDC_PROTOCOL_NUMBER = env.str("EDC_PROTOCOL_NUMBER")
EDC_PROTOCOL_PROJECT_NAME = env.str("EDC_PROTOCOL_PROJECT_NAME")
EDC_PROTOCOL_PROJECT_NAME = "EFFECT"
EDC_PROTOCOL_STUDY_OPEN_DATETIME = get_datetime_from_env(
    *env.list("EDC_PROTOCOL_STUDY_OPEN_DATETIME")
)
EDC_PROTOCOL_STUDY_CLOSE_DATETIME = get_datetime_from_env(
    *env.list("EDC_PROTOCOL_STUDY_CLOSE_DATETIME")
)
EDC_PROTOCOL_TITLE = env.str("EDC_PROTOCOL_TITLE")


SARSCOV2_REDIRECT_URL_NAME = "screening_listboard_url"

# static
if env("AWS_ENABLED"):
    # see
    # https://www.digitalocean.com/community/tutorials/
    # how-to-set-up-a-scalable-django-app-with-digitalocean-
    # managed-databases-and-spaces
    AWS_ACCESS_KEY_ID = env.str("AWS_ACCESS_KEY_ID")
    AWS_DEFAULT_ACL = "public-read"
    AWS_SECRET_ACCESS_KEY = env.str("AWS_SECRET_ACCESS_KEY")
    AWS_STORAGE_BUCKET_NAME = env.str("AWS_STORAGE_BUCKET_NAME")
    AWS_S3_CUSTOM_DOMAIN = env.str("AWS_S3_CUSTOM_DOMAIN")
    AWS_S3_ENDPOINT_URL = env.str("AWS_S3_ENDPOINT_URL")
    AWS_S3_OBJECT_PARAMETERS = {"CacheControl": "max-age=86400"}
    AWS_LOCATION = env.str("AWS_LOCATION")
    AWS_IS_GZIPPED = True
    STATICFILES_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
    STATIC_URL = f"{os.path.join(AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)}/"
    STATIC_ROOT = ""
else:
    # run collectstatic, check nginx LOCATION
    STATIC_URL = env.str("DJANGO_STATIC_URL")
    STATIC_ROOT = env.str("DJANGO_STATIC_ROOT")

SENTRY_DSN = env("SENTRY_DSN")

if SENTRY_ENABLED and SENTRY_DSN:
    import sentry_sdk

    # from sentry_sdk.integrations.django import DjangoIntegration

    sentry_sdk.init(
        dsn=SENTRY_DSN,
        integrations=[sentry_sdk.integrations.django.DjangoIntegration()],
        traces_sample_rate=1.0,
        send_default_pii=True,
    )

if env("DJANGO_LOGGING_ENABLED"):
    from .logging import LOGGING  # noqa

# CELERY
# see docs on setting up the broker
CELERY_ENABLED = env("CELERY_ENABLED")
if CELERY_ENABLED:
    CELERY_BROKER_USER = env.str("CELERY_BROKER_USER")
    CELERY_BROKER_PASSWORD = env.str("CELERY_BROKER_PASSWORD")
    CELERY_BROKER_HOST = env.str("CELERY_BROKER_HOST")
    CELERY_BROKER_PORT = env.str("CELERY_BROKER_PORT")
    if DEBUG:
        CELERY_BROKER_VHOST = f"{APP_NAME}_debug"
    elif LIVE_SYSTEM:
        CELERY_BROKER_VHOST = f"{APP_NAME}_production"
    else:
        CELERY_BROKER_VHOST = f"{APP_NAME}_uat"
        CELERY_BROKER_URL = (
            f"amqp://{CELERY_BROKER_USER}:{CELERY_BROKER_PASSWORD}@"
            f"{CELERY_BROKER_HOST}:{CELERY_BROKER_PORT}/{CELERY_BROKER_VHOST}"
        )
        DJANGO_CELERY_RESULTS_TASK_ID_MAX_LENGTH = 191
        CELERY_RESULT_BACKEND = "django-db"
        #     CELERY_QUEUES = (
        #         Queue('high', Exchange('high'), routing_key='high'),
        #         Queue('normal', Exchange('normal'), routing_key='normal'),
        #         Queue('low', Exchange('low'), routing_key='low'),
        #     )
        #     CELERY_DEFAULT_QUEUE = 'normal'
        #     CELERY_DEFAULT_EXCHANGE = 'normal'
        #     CELERY_DEFAULT_ROUTING_KEY = 'normal'
        #     CELERY_ROUTES = {
        #         'edc_data_manager.tasks.*': {'queue': 'normal'},
        #     }

EDC_APPOINTMENT_APPT_REASON_CHOICES = (
    (SCHEDULED_APPT, "Scheduled visit (study)"),
    (UNSCHEDULED_APPT, "Routine / Unscheduled (non-study)"),
)


if "test" in sys.argv:

    class DisableMigrations:
        def __contains__(self, item):
            return True

        def __getitem__(self, item):
            return None

    MIGRATION_MODULES = DisableMigrations()
    PASSWORD_HASHERS = ("django.contrib.auth.hashers.MD5PasswordHasher",)
    DEFAULT_FILE_STORAGE = "inmemorystorage.InMemoryStorage"

    if env("SAUCE_ENABLED"):
        SAUCE_USERNAME = env.str("SAUCE_USERNAME")
        SAUCE_ACCESS_KEY = env.str("SAUCE_ACCESS_KEY")
