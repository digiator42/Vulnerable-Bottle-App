import os

# app settings
DEBUG = True
RELOADER = True
PORT = 8080
HOST = "0.0.0.0"

# root directory
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# static files & uploads
STATIC_DIR = './static'
MEDIA_DIR = './media'

# levels
DEFAULT_LEVEL = "weak"
MEDIUM_LEVEL = "medium"
STRONG_LEVEL = "strong"

LEVELS = (DEFAULT_LEVEL, MEDIUM_LEVEL, STRONG_LEVEL)

# Session settings
session_opts = {
    'session.type': 'file',
    'session.data_dir': './data',
    'session.auto': True,
    'session.cookie_expires': True,
}
