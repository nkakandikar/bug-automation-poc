"""
Unit tests for Calculator
These tests will initially fail for the buggy functions
"""

import unittest
import math
from calculator import Calculator


class TestCalculator(unittest.TestCase):
    """Test cases for Calculator class"""
    
    def setUp(self):
        """Set up test calculator instance"""
        self.calc = Calculator()
    
    def test_add(self):
        """Test addition"""
        self.assertEqual(self.calc.add(5, 3), 8)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
    
    def test_subtract(self):
        """Test subtraction"""
        self.assertEqual(self.calc.subtract(10, 4), 6)
        self.assertEqual(self.calc.subtract(5, 10), -5)
        self.assertEqual(self.calc.subtract(0, 0), 0)
    
    def test_multiply(self):
        """Test multiplication"""
        self.assertEqual(self.calc.multiply(6, 7), 42)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(0, 100), 0)
    
    def test_divide(self):
        """Test division"""
        self.assertEqual(self.calc.divide(15, 3), 5)
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertAlmostEqual(self.calc.divide(7, 3), 2.333, places=2)
    
    def test_divide_by_zero(self):
        """
        Test division by zero
        This test will FAIL initially - the bug needs to be fixed!
        """
        # After fix, should raise ValueError or return a specific error
        with self.assertRaises((ValueError, ZeroDivisionError)):
            self.calc.divide(10, 0)
    
    def test_power(self):
        """Test power operation"""
        self.assertEqual(self.calc.power(2, 3), 8)
        self.assertEqual(self.calc.power(5, 2), 25)
        self.assertEqual(self.calc.power(10, 0), 1)
    
    def test_sqrt(self):
        """Test square root"""
        self.assertEqual(self.calc.sqrt(16), 4)
        self.assertEqual(self.calc.sqrt(25), 5)
        self.assertAlmostEqual(self.calc.sqrt(2), 1.414, places=2)
    
    def test_sqrt_negative(self):
        """
        Test square root of negative number
        This test will FAIL initially - the bug needs to be fixed!
        """
        # After fix, should raise ValueError
        with self.assertRaises(ValueError):
            self.calc.sqrt(-4)
    
    def test_percentage(self):
        """Test percentage calculation"""
        self.assertEqual(self.calc.percentage(150, 20), 30)
        self.assertEqual(self.calc.percentage(100, 50), 50)
        self.assertEqual(self.calc.percentage(200, 10), 20)
    
    def test_absolute(self):
        """Test absolute value"""
        self.assertEqual(self.calc.absolute(-5), 5)
        self.assertEqual(self.calc.absolute(5), 5)
        self.assertEqual(self.calc.absolute(0), 0)


if __name__ == '__main__':
    unittest.main()
