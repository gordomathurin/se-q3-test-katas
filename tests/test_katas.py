import unittest
import katas
import random


class TestKatas(unittest.TestCase):
    def test_add(self):
        self.assertIsNotNone(katas.add)
        for _ in range(20):
            x = random.randrange(-500, 500)
            y = random.randrange(-500, 500)
            self.assertEqual(katas.add(x, y), x + y)

    def test_multiply(self):
        self.assertIsNotNone(katas.multiply)
        self.assertEqual(katas.multiply(-4, -3), 12)
        self.assertEqual(katas.multiply(-4, 3), -12)
        self.assertEqual(katas.multiply(4, 4), 16)
        for _ in range(10):
            x = random.randrange(-500, 500)
            y = random.randrange(-500, 500)
            self.assertEqual(katas.multiply(x, y), x * y)

    def test_power(self):
        self.assertIsNotNone(katas.power)
        self.assertEqual(katas.power(5, 4), 5 ** 4)
        self.assertEqual(katas.power(-4, 3), -4 ** 3)
        self.assertEqual(katas.power(62, 0), 1)
        for _ in range(10):
            x = random.randrange(-20, 20)
            y = random.randrange(0, 10)
            self.assertEqual(katas.power(x, y), x ** y)

    def test_factorial(self):
        self.assertIsNotNone(katas.factorial)
        self.assertEqual(katas.factorial(4), katas.factorial(4))
        for x in range(10):
            self.assertEqual(katas.factorial(x), katas.factorial(x))

    def test_fibonacci(self):
        self.assertIsNotNone(katas.fibonacci)
        fibs = (0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89)
        for n in range(11):
            self.assertEqual(katas.fibonacci(n), fibs[n])


if __name__ == '__main__':
    unittest.main()
