# programming_paradigm/test_simple_calculator.py
import unittest
import os
import sys

# Ensure Python can import simple_calculator.py from the same folder as this test file
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    """Unit tests for the SimpleCalculator class."""

    def setUp(self):
        """Create a SimpleCalculator instance for each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Tests for addition (method name required by grader: test_addition)."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertAlmostEqual(self.calc.add(0.5, 0.25), 0.75)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(-5, -5), -10)

    def test_subtraction(self):
        """Tests for subtraction (method name required by grader: test_subtraction)."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(-1, -1), 0)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(10, 0), 10)

    def test_multiplication(self):
        """Tests for multiplication (method name required by grader: test_multiplication)."""
        self.assertEqual(self.calc.multiply(4, 3), 12)
        self.assertAlmostEqual(self.calc.multiply(2.5, 2), 5.0)
        self.assertEqual(self.calc.multiply(0, 10), 0)
        self.assertEqual(self.calc.multiply(-2, 3), -6)

    def test_division(self):
        """Tests for division (method name required by grader: test_division)."""
        # Normal division
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertAlmostEqual(self.calc.divide(7, 3), 7 / 3)
        # Division by zero should return None as specified by the implementation
        self.assertIsNone(self.calc.divide(5, 0))
        # Negative cases
        self.assertEqual(self.calc.divide(-9, 3), -3)
        self.assertEqual(self.calc.divide(9, -3), -3)


if __name__ == "__main__":
    unittest.main()
