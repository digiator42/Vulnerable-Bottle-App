from pathlib import PurePath

# app settings
DEBUG = True
RELOADER = True
PORT = 8000
HOST = '0.0.0.0'

# root directory
ROOT_DIR = PurePath(__file__).parent.parent

# static files & uploads
STATIC_DIR = './static'
MEDIA_DIR = './media'

# levels
DEFAULT_LEVEL = 'weak'
MEDIUM_LEVEL = 'medium'
STRONG_LEVEL = 'strong'

LEVELS = (DEFAULT_LEVEL, MEDIUM_LEVEL, STRONG_LEVEL)

# Session settings
session_opts = {
    'session.type': 'file',
    'session.data_dir': './data',
    'session.auto': True,
    'session.cookie_expires': True,
}

KEY = b'8fofGbsrUJuj9P9Za9lVZhjVEzZohhiu4cfSWc5cgLo='