DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = 'booklist'
DATABASE_USER = 'booklist'
DATABASE_PASSWORD = 'elektric7'

AUTHENTICATION_BACKENDS = (
    'infxbooklist.uciwebauth.DjangoBackend',
)

TEMPLATE_DIRS = (
    '/root/project/infxbooklist/templates'
)

ADMIN_MEDIA_PREFIX = '/admin/media/'

MEDIA_ROOT='/root/project/infxbooklist/'


ADMIN_UCINETIDS = ('kaufmans', 'kay', 'royr', 'sparksc')
