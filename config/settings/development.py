"""
Development settings for College Library Portal.
"""
from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

# Console email backend for viewing registration/notification emails in dev
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

