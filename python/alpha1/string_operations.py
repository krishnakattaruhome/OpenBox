# string_operations.py
def reverse_string(s):
    """Function to reverse a string."""
    return s[::-1]

def to_uppercase(s):
    """Function to convert a string to uppercase."""
    return s.upper()

class StringManipulator:
    """A class to manipulate strings."""
    def __init__(self, text):
        self.text = text

    def reverse(self):
        """Method to reverse the text."""
        self.text = self.text[::-1]
        return self.text

    def to_uppercase(self):
        """Method to convert the text to uppercase."""
        self.text = self.text.upper()
        return self.text