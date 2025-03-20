import unittest
from app import home  # Ensure that the `app.py` is in the same directory or accessible

class TestApp(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(home(), "Hello, Dockerized World!")  # Fixed the typo here

if __name__ == "__main__":
    unittest.main()
 