#Begin with the day 13 of pratice problem solving - Sumit Shukla
# 1. Write a Python test class using unittest.TestCase to test a function add(a, b) which returns the sum of two numbers.Include at least two test methods to verify correct addition behavior.

import unittest
def addition(a, b):
    return a + b

class TestAddition(unittest.TestCase):
    def test_add(self):
        self.assertEqual(addition(2, 3), 5)
        self.assertEqual(addition(-1, 1), 0)    

if __name__ == '__main__':
    unittest.main()

# 2. Create a function is_even(n) that returns True if the number is even, otherwise False.Now write a unit test using unittest with multiple test cases to validate it (e.g., test with 2, 3, 0, -4, etc.).

import unittest
def is_even(n):
    return n % 2 == 0

import unittest

class TestIsEvenFunction(unittest.TestCase):
    def test_even_number(self):
        self.assertTrue(is_even(4)) 
    def test_odd_number(self):
        self.assertFalse(is_even(5)) 
    def test_zero(self):
        self.assertTrue(is_even(0)) 
    def test_negative_even_number(self):
        self.assertTrue(is_even(-2))  
    def test_negative_odd_number(self):
        self.assertFalse(is_even(-3)) 
if __name__ == '__main__':
    unittest.main()


# 3. Write a Python module that includes both:

# · A function factorial(n) that returns the factorial of a non-negative integer.

# · A unittest-based test class to test the function, and run it using unittest.main().


