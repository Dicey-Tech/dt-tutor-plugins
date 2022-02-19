from ..production import *

{% include "dt_learninghub/apps/settings/partials/common.py" %}

BACKEND_SERVICE_EDX_OAUTH2_KEY = "{{ DT_CLASSROOM_OAUTH2_KEY }}"
BACKEND_SERVICE_EDX_OAUTH2_SECRET = "{{ DT_CLASSROOM_OAUTH2_SECRET }}"
BACKEND_SERVICE_EDX_OAUTH2_PROVIDER_URL = "http://lms:8000/oauth2"

SOCIAL_AUTH_EDX_OAUTH2_KEY = "{{ DT_CLASSROOM_OAUTH2_KEY_SSO }}"
SOCIAL_AUTH_EDX_OAUTH2_SECRET = "{{ DT_CLASSROOM_OAUTH2_SECRET_SSO }}"
SOCIAL_AUTH_EDX_OAUTH2_ISSUER = "{{ 'https' if ENABLE_HTTPS else 'http' }}://{{ LMS_HOST }}"
SOCIAL_AUTH_EDX_OAUTH2_URL_ROOT = SOCIAL_AUTH_EDX_OAUTH2_ISSUER
SOCIAL_AUTH_EDX_OAUTH2_PUBLIC_URL_ROOT = SOCIAL_AUTH_EDX_OAUTH2_ISSUER
SOCIAL_AUTH_EDX_OAUTH2_LOGOUT_URL = SOCIAL_AUTH_EDX_OAUTH2_ISSUER + "/logout"

SOCIAL_AUTH_REDIRECT_IS_HTTPS = {% if ENABLE_HTTPS %}True{% else %}False{% endif %}

CORS_ORIGIN_WHITELIST.append("{{ 'https' if ENABLE_HTTPS else 'http' }}://{{ MFE_HOST }}")

CSRF_TRUSTED_ORIGINS.append("{{ MFE_HOST }}")

{{ patch("dt-classrooms-production-settings") }}