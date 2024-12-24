Control Flow:
if, elif, else: Conditional statements
for, while: Looping statements
break, continue: Loop control
pass: Placeholder statement
try, except, finally: Exception handling
raise: Raising exceptions
with: Context management

# Check conditions using if, elif, and else
if age < 18:
    print("You are a minor.")
elif age >= 18 and age <= 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")


# Using a for loop with break and continue
print("For loop with break and continue:")
for i in range(1, 11):
    if i == 5:
        print("Breaking out of the loop at i =", i)
        break  # Exit the loop when i equals 5
    elif i % 2 == 0:
        print("Skipping even number:", i)
        continue  # Skip the even numbers
    print("Processing number:", i)


# Using a while loop with break and continue
print("\nWhile loop with break and continue:")
j = 1
while j <= 10:
    if j == 7:
        print("Breaking out of the loop at j =", j)
        break  # Exit the loop when j equals 7
    elif j % 2 == 0:
        print("Skipping even number:", j)
        j += 1  # Increment before continue
        continue  # Skip the even numbers
    print("Processing number:", j)
    j += 1  # Increment after processing


# Example of using pass in a loop
for i in range(5):
    if i == 3:
        pass  # Do nothing when i equals 3
    else:
        print("Processing number:", i)

# Example of using with for file handling
with open("example.txt", "w") as file:
    file.write("Hello, world!")  # Writing to the file
    
# Example using raise, try, except, and finally
def divide_numbers(a, b):
    try:
        # Try to divide numbers
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")  # Raising an exception manually
        result = a / b
        print("Division result:", result)
    except ZeroDivisionError as e:
        # Handling division by zero error
        print(f"Error: {e}")
    except Exception as e:
        # Handling any other exceptions
        print(f"An unexpected error occurred: {e}")
    finally:
        # This block will always execute, no matter what
        print("Execution completed.")





Data Types:
int, float, complex: Numeric types
str: String type
bool: Boolean type
list, tuple, dict, set: Collection types
None: Special value indicating no value

Functions and Classes:
def: Defining functions
class: Defining classes
lambda: Anonymous functions
return: Returning values from functions
yield: Generator functions


# Using def to define a function
def square(x):
    return x * x  # Using return to send back a result

# Using a class to define an object
class Calculator:
    def __init__(self, value):
        self.value = value
    
    def add(self, other_value):
        return self.value + other_value  # Method using return
    
    def multiply(self, other_value):
        return self.value * other_value  # Method using return

# Using lambda for a simple function
add_five = lambda x: x + 5  # Lambda function that adds 5 to the input

# Using yield in a generator function
def count_up_to(n):
    count = 1
    while count <= n:
        yield count  # Yield the current count and pause the function until next call
        count += 1


Modules and Imports:
import: Importing modules
from: Importing specific attributes from modules
as: Aliasing imports
global, nonlocal: Variable scope

# Using global to modify a variable outside a function
x = 10  # Global variable

def modify_global():
    global x  # Declare x as global to modify it
    x = 20  # Modify the global variable

print("Before modifying global x:", x)  # x is 10
modify_global()
print("After modifying global x:", x)  # x is now 20


# Using nonlocal to modify a variable in an enclosing scope (but not global)
def outer_function():
    y = 5  # Variable in the enclosing function

    def inner_function():
        nonlocal y  # Declare y as nonlocal to modify it
        y = 10  # Modify the variable in the enclosing scope

    print("Before modifying nonlocal y:", y)  # y is 5
    inner_function()
    print("After modifying nonlocal y:", y)  # y is now 10

outer_function()


Boolean Logic:
and, or, not: Logical operators
is, in: Membership and identity operators

Asynchronous Programming:
async, await: Asynchronous functions and operations

Miscellaneous:
True, False: Boolean values
del: Deleting objects
assert: Debugging assertions


