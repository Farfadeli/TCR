import unittest
from main import divide

class CalculMethod(unittest.TestCase):
    def test_additionner(self):
        self.assertEqual(divide(122, 2) , 61)

if __name__ == '__main__':
    unittest.main()