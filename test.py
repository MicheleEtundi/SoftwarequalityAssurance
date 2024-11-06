# test_app.py
import unittest
from app import app


class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        """Set up the test client before each test."""
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        """Test the home route."""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, "Hello level 400 FET, Quality Assurance everything is good!")


if __name__ == '__main__':
    unittest.main()
    