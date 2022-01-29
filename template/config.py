import os
import secrets


class Config:

    # general settings
    WTF_CSRF_ENABLED = False
    SECRET_KEY                 = secrets.token_urlsafe()
    SESSION_TYPE               = os.environ.get('SESSION_TYPE', 'null') # redis perferred?


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    EXPLAIN_TEMPLATE_LOADING = True

    SECRET_KEY                 = 'rn4TCYBn25mvaUNkdi-p6XrbwDxcdG6xt72oIXRtOkc'


class TestingConfig(Config):
    TESTING = True
