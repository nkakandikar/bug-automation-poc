"""
Simple Calculator Module
This is a basic calculator with intentional bugs for POC testing
"""

import math


class Calculator:
    """A simple calculator class with basic operations"""
    
    def add(self, a, b):
        """Add two numbers"""
        return a + b
    
    def subtract(self, a, b):
        """Subtract b from a"""
        return a - b
    
    def multiply(self, a, b):
        """Multiply two numbers"""
        return a * b
    
    def divide(self, a, b):
        """
        Divide a by b
        BUG: This will crash if b is 0
        """
        # TODO: Add zero division handling
        return a / b
    
    def power(self, base, exponent):
        """Raise base to the power of exponent"""
        return base ** exponent
    
    def sqrt(self, number):
        """
        Calculate square root of a number
        BUG: This will crash for negative numbers
        """
        # TODO: Add negative number handling
        return math.sqrt(number)
    
    def percentage(self, value, percent):
        """Calculate percentage of a value"""
        return (value * percent) / 100
    
    def absolute(self, number):
        """Return absolute value of a number"""
        return abs(number)


def main():
    """Demo function to show calculator usage"""
    calc = Calculator()
    
    print("Calculator Demo")
    print("=" * 40)
    
    # These work fine
    print(f"5 + 3 = {calc.add(5, 3)}")
    print(f"10 - 4 = {calc.subtract(10, 4)}")
    print(f"6 * 7 = {calc.multiply(6, 7)}")
    print(f"15 / 3 = {calc.divide(15, 3)}")
    print(f"2 ^ 3 = {calc.power(2, 3)}")
    print(f"sqrt(16) = {calc.sqrt(16)}")
    print(f"20% of 150 = {calc.percentage(150, 20)}")
    print(f"|-5| = {calc.absolute(-5)}")
    
    # These will cause bugs (commented out to prevent crashes)
    # print(f"10 / 0 = {calc.divide(10, 0)}")  # BUG: ZeroDivisionError
    # print(f"sqrt(-4) = {calc.sqrt(-4)}")     # BUG: ValueError


if __name__ == "__main__":
    main()
