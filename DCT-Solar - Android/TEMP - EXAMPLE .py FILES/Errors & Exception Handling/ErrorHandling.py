# Example 1 - Basic Error Handling

try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))
    result = num1 / num2
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot Divide by zero!")
except ValueError:
    print("Error: Invalid Input. Please enter a valid number.")


# Example 2 - Handling Multiple Exceptions

try:
    file = open('non_existent_file.txt', 'r')
    content = file.read()
    file.close()
except (FileNotFoundError, IOError):
    print("Error: File not found or cannot be read.")


# Example 3 - Handling Specific Exceptions

try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
except ArithmeticError:
    print("Arithmetic error occurred")


# Example 4 - Using Else and Finally

try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid input")
else:
    print("You entered:", num)
finally:
    print("Execution complete")


# Example 5 - Raising Exceptions

try:
    x = int(input("Enter a number: "))
    if x < 0:
        raise ValueError("Number must be positive")
except ValueError as ve:
    print(ve)


# Example 6 - Custom Exception Classes

class MyCustomError(Exception):
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return repr(self.value)


try:
    raise MyCustomError("An error occurred")
except MyCustomError as e:
    print("Custom error raised:", e.value)


# Example 7 - Handling Exceptions in Loops

data = [5, 0, 10, 2]
for num in data:
    try:
        result = 10 / num
        print("Result:", result)
    except ZeroDivisionError:
        print("Cannot divide by zero")


# Example 8 - Handling Exceptions in Functions

def divide(x, y):
    try:
        result = x / y
        return result
    except ZeroDivisionError:
        return "Cannot divide by zero"

print(divide(10, 0))