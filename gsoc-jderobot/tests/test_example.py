import unittest
from src.example import greet

class TestExample(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("Alice"), "Hello, Alice! Welcome to Robotics Academy.")

if __name__ == "__main__":
    unittest.main()
