# main.py
from mypackage.math_operations import add, multiply, Calculator
from mypackage.string_operations import reverse_string, StringManipulator
from mypackage.utils import print_welcome_message

# Using functions from math_operations
result_add = add(5, 3)
result_multiply = multiply(4, 2)

# Using Calculator class
calc = Calculator(10)
calc_result_add = calc.add(5)
calc_result_multiply = calc.multiply(2)

# Using functions from string_operations
reversed_string = reverse_string("hello")

# Using StringManipulator class
manipulator = StringManipulator("python")
manipulator_reversed = manipulator.reverse()
manipulator_upper = manipulator.to_uppercase()

# Using utils
print_welcome_message("Alice")
string_length = get_length_of_string("hello world")

# Print the results
print(f"Addition result: {result_add}")
print(f"Multiplication result: {result_multiply}")
print(f"Calculator add result: {calc_result_add}")
print(f"Calculator multiply result: {calc_result_multiply}")
print(f"Reversed string: {reversed_string}")
print(f"StringManipulator reversed: {manipulator_reversed}")
print(f"StringManipulator upper: {manipulator_upper}")
print(f"Length of string: {string_length}")
