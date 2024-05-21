import unittest
from main import additionner

class CalculMethod(unittest.TestCase):
    def test_additionner(self):
        self.assertEqual(additionner(2, 3) , 5)

if __name__ == '__main__':
    unittest.main()