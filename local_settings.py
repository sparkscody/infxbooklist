DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = '/usr/local/lib/python2.7/site-packages/django/db/booklist.db'
DDATABASE_USER = 'booklist'      # Not used with sqlite3.
DATABASE_PASSWORD = 'elektric7' # Not used with sqlite3.
DATABASE_HOST = '24.30.191.233'              # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = '3457'              # Set to empty string for default. Not used with sqlite3.

AUTHENTICATION_BACKENDS = (
    'infxbooklist.uciwebauth.DjangoBackend',
)

TEMPLATE_DIRS = (
    '/root/project/infxbooklist/templates'
)

ADMIN_MEDIA_PREFIX = '/admin/media/'

MEDIA_ROOT='/root/project/infxbooklist/'


ADMIN_UCINETIDS = ('kaufmans', 'kay', 'royr', 'sparksc')
