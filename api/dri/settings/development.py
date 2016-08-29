# Load defaults and local_vars in order to then add/override with development-only settings
from dri.settings.defaults import *
from dri.settings.local_vars import *

ALLOWED_HOSTS = '*'
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True

DEBUG = True

# INSTALLED_APPS.extend([
#     'debug_toolbar',
# ])
