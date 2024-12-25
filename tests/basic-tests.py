import unittest
import sys
import os
import requests
import pickle
import json
sys.path.append(os.path.abspath(''))
from config.settings import PORT
from utils.main import PY_EXT
from config.routes import TRIGGER_ROUTES, ROOT_ROUTES
from triggers.deserialization import (
    weak_deserialization, medium_deserialization, strong_deserialization
)
from dotenv import load_dotenv
import os

load_dotenv()

username = os.getenv('ADMIN_USERNAME')
password = os.getenv('ADMIN_PASSWORD')

def _make_request(self, url, session):
    try:
        response = session.get(url, timeout=1)
        response.raise_for_status()
    except Exception as e:
        # print(str(e)[:20] + '...')
        print('Dead route: ', url)    

class TestRoutes(unittest.TestCase):
    data = {'username': username, 'password': password}
    global session
    session = requests.Session()
    response = session.post(f'http://localhost:{PORT}/login', data=data, timeout=2)
    response.raise_for_status()    

    def test_home(self):
        for route in ROOT_ROUTES:
            url = f'http://localhost:{PORT}/{route}'
            _make_request(self, url, session)

class Test_Trigger_Routes(unittest.TestCase):
    def test_triggers(self):
        for module, route in TRIGGER_ROUTES.items():
            url = f'http://localhost:{PORT}/{module}/{route[:PY_EXT].replace('-', '_')}'
            _make_request(self, url, session)

class Test_Deserialization(unittest.TestCase):
    def test_deserialization_weak(self):
        payload = {"input": "test"}
        byte_payload = pickle.dumps(payload)
        result = weak_deserialization({'input': str(byte_payload)})
        self.assertEqual(result, payload)

    def test_deserialization_medium(self):
        payload = {"input": "test"}
        byte_payload = pickle.dumps(payload)
        result = medium_deserialization({'input': str(byte_payload)})
        self.assertEqual(result, payload)

    def test_deserialization_strong(self):
        payload = {"input": "test"}
        byte_payload = pickle.dumps(payload)
        result = strong_deserialization({'input': str(byte_payload)})
        self.assertNotEqual(result, payload)

    def test_deserialization_strong2(self):
        payload = {"input": "test"}
        byte_payload = json.dumps(payload)
        result = strong_deserialization({'input': str(byte_payload)})
        self.assertNotEqual(result, payload)

if __name__ == '__main__':
    unittest.main()