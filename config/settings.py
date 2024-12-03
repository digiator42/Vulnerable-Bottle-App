import os

DEBUG = True
RELOADER = True
PORT = 6060
HOST = "localhost"
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_LEVEL = "weak"
MEDIUM_LEVEL = "medium"
LEVELS = (DEFAULT_LEVEL, MEDIUM_LEVEL)

# Session settings
session_opts = {
    'session.type': 'file',
    'session.data_dir': './data',
    'session.auto': True,
    'session.cookie_expires': True,
}
