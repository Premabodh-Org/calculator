import unittest
from logic import add, subtract, multiply, divide, cube

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 2), 4)
        
    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(-1, 1), -2)
        self.assertEqual(subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(multiply(10, 5), 50)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(0, 5), 0)

    def test_divide(self):
        self.assertEqual(divide(10, 5), 2)
        self.assertEqual(divide(-1, 1), -1)
        self.assertEqual(divide(5, 2), 2.5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_cube(self):
        self.assertEqual(cube(2), 8)
        self.assertEqual(cube(-3), -27)
        self.assertEqual(cube(0), 0)
        self.assertEqual(cube(1), 1)

if __name__ == __main__:
    unittest.main()