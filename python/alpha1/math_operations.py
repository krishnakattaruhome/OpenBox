# math_operations.py
def add(a, b):
    """Function to add two numbers."""
    return a + b

def multiply(a, b):
    """Function to multiply two numbers."""
    return a * b

class Calculator:
    """A simple calculator class."""
    def __init__(self, value):
        self.value = value

    def add(self, other_value):
        """Method to add a number to the current value."""
        self.value += other_value
        return self.value

    def multiply(self, other_value):
        """Method to multiply the current value by another number."""
        self.value *= other_value
        return self.value