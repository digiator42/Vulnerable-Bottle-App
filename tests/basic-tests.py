import unittest
import sys
import os
import requests
import pickle
import json
sys.path.append(os.path.abspath(''))
from config.settings import PORT
from config.routes import TRIGGER_ROUTES, ROOT_ROUTES
from triggers.deserialization import weak_deserialization, medium_deserialization, strong_deserialization

class TestRoutes(unittest.TestCase):
    def test_home(self):
        for route in ROOT_ROUTES:
            response = requests.get(f'http://localhost:{PORT}/{route}')
            self.assertEqual(response.status_code, 200)

class Test_Trigger_Routes(unittest.TestCase):
    def test_triggers(self):
        for route in TRIGGER_ROUTES:
            response = requests.get(f'http://localhost:{PORT}/{route}')
            self.assertEqual(response.status_code, 200)

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

    def test_deserialization_strong(self):
        payload = {"input": "test"}
        byte_payload = json.dumps(payload)
        result = strong_deserialization({'input': str(byte_payload)})
        self.assertNotEqual(result, payload)

if __name__ == '__main__':
    unittest.main()