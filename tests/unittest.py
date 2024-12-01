import unittest
import sys
import os
import requests
sys.path.append(os.path.abspath('../'))

from config.settings import PORT, HOST
from config.routes import TRIGGER_ROUTES, ROOT_ROUTES


class TestRoutes(unittest.TestCase):
    def test_home(self):
        for route in ROOT_ROUTES:
            response = requests.get(f'http://{HOST}:{PORT}/{route}')
            self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()