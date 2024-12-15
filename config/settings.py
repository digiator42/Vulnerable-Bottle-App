import os

# app settings
DEBUG = True
RELOADER = True
PORT = 8088
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

database_users = {
    "admin": {"role": "admin", "password": "e85eee9629076b118449949f1162fc7a"},
    "Alice": {"role": "user", "password": "0571749e2ac330a7455809c6b0e7af90"},
    "Bob": {"role": "user", "password": "3899dcbab79f92af727c2190bbd8abc5"},
    "Charlie": {"role": "user", "password": "8afa847f50a716e64932d995c8e7435a"},
    "David": {"role": "user", "password": "25f9e794323b453885f5181f1b624d0b"},
    "Eve": {"role": "admin", "password": "54bf3dc2c4f98fabdf78b7216c0ae888455d009a"} # sha1
}