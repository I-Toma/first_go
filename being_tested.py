# In programming, a variable is a named storage location that can hold a value. It's like a container that you can use to store and manipulate data in your program.

# In Python, you declare a variable by giving it a name and assigning a value to it. For example:

variable = 12
# In this case, you've created a variable named variable and assigned the value 12 to it. Well done!

# Let's move on to the next question. How would you print the value of this variable to the console in Python?

print(variable)
# This will print the value stored in the variable to the console.

# In Python, variables can hold different types of data. The basic data types in Python include:

int = Integer (whole number) # type: ignore
float = Floating-point number (decimal) # type: ignore
str = String (sequence of characters) # type: ignore
bool = Boolean (True or False) # type: ignore

number = 42                # data type is integer

pi = 3.14                  # data type is float

message = "Hello, Python!" # data type string

is_python_fun = True       # data type boolean

# In Python, you can perform various operations on variables and values. Let's say you have two variables:

a = 10
b = 5
# Now, can you tell me the result of the following operations:
a + b # type: ignore
a - b # type: ignore
a * b # type: ignore
a / b # type: ignore
a // b (floor division) # type: ignore
a % b (modulus) # type: ignore
a ** b (exponentiation) # type: ignore
# Feel free to take your time and calculate each result!

a + b = 15, a - b = 5, a * b = 50, a / b = 2, a // b = 2, a % b = 0, a ** b = 100000 # type: ignore

a + b: # Addition - Result: 15 # type: ignore
a - b: # Subtraction - Result: 5 # type: ignore
a * b: # Multiplication - Result: 50 # type: ignore
a / b: # Division - Result: 2.0 (in Python 3, division always returns a float) # type: ignore
a // b: # Floor Division - Result: 2 (returns the quotient, discarding the remainder) # type: ignore
a % b: # Modulus - Result: 0 (returns the remainder of the division) # type: ignore
a ** b: # Exponentiation - Result: 100000 # type: ignore

# Alright, let's delve into another important topic: conditional statements.

# In Python, you use conditional statements to make decisions in your code. The basic structure includes the if, elif (optional), and else (optional) statements. Here's an example:

x = 10

if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")
#In this example, the program checks the value of x:

#If x is greater than 0, it prints "x is positive."
#If x is equal to 0, it prints "x is zero."
#If neither of the above conditions is true, it prints "x is negative."

#Now, let's try a small exercise. Can you write a piece of code that takes a number as input and prints whether it's an even or odd number? If you need help, feel free to ask!

a = 8
if a % 2 == 0:
    print("is an even number")
else:
    print("is an odd number")

#Excellent! You've successfully written a piece of code to determine whether a number is even or odd. Your code checks if the remainder of dividing a by 2 is equal to 0. If true, it prints "is an even number," otherwise, it prints "is an odd number." Well done!

#In Python, there are two primary types of loops: for loops and while loops.

#For Loops:
#A for loop is used to iterate over a sequence (such as a list, tuple, or string) or other iterable objects. Here's an example:

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
#This loop iterates through each element in the fruits list and prints each fruit.

#While Loops:
#A while loop repeats a block of code as long as a certain condition is true. Here's an example:

count = 0
while count < 5:
    print(count)
    count += 1
#This loop prints the value of count as long as it is less than 5.

#Now, let's try a small exercise. Can you write a for loop that prints the square of each number in the range from 1 to 5? If you need help, feel free to ask!
for number in range(1, 6):
    square = number ** 2
    print(f"The square of {number} is {square}")
# Here's a quick breakdown of your code:
for number in range(1, 6): # This loop iterates over the numbers 1 to 5 (inclusive).
square = number ** 2: # Calculates the square of each number. # type: ignore
print(f"The square of {number} is {square}") # Prints the result for each iteration.

# Functions
# In Python, a function is a block of code that performs a specific task. Functions are defined using the def keyword. Here's a simple example:

def greet(name):
    print(f"Hello, {name}!")

# Call the function
greet("Alice")
# In this example, we've defined a function named greet that takes a parameter name and prints a greeting. The function is then called with the argument "Alice."

# Write a function named calculate_area that takes the radius of a circle as a parameter and prints the area of the circle? The formula for the area of a circle is area = π * r^2. If you need help, feel free to ask!
# area = π * r^2
# area = pi * radius square

def calculate_area(r):
    π = 3.14
    area = π * r**2
    print(area)
# Example usage
calculate_area(3)

# Let's try creating a function that calculates the area of a rectangle. The formula for the area of a rectangle is area = length * width. Can you write a function named calculate_rectangle_area that takes length and width as parameters and returns the area of the rectangle?

def calculate_rectangle_area(length, width):
    area = length * width
    return area
# Example usage
length = 100
width = 50

rectangle_area = calculate_rectangle_area(length, width)

print(f"The area of a rectangle with length {length} and width {width} is {rectangle_area}")

# Temperature Conversion:
# Write a function that converts temperatures between Celsius and Fahrenheit. The formula for conversion is:
# Fahrenheit to Celsius: (F - 32) * 5/9
# Celsius to Fahrenheit: (C * 9/5) + 32

def temperature_conversion(celsius, fahrenheit):
    converted_celsius = (celsius * 9/5) + 32
    converted_fahrenheit = (fahrenheit - 32) * 5/9
    return converted_celsius, converted_fahrenheit

# Example usage
celsius = 30
fahrenheit = 80
converted_temperature = temperature_conversion(celsius, fahrenheit)

print(f"{celsius} Celsius is equal to {converted_temperature[0]:.2f} Fahrenheit")
print(f"{fahrenheit} Fahrenheit is equal to {converted_temperature[1]:.2f} Celsius")

# List Filtering:
# Write a function that takes a list of numbers and returns a new list containing only the even numbers.

def list_of_numbers(num_list):
    new_list = []
    for num in num_list:
        if num % 2 == 0:
            new_list.append(num)
    return new_list
# Example usage
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_list = list_of_numbers(numbers)
print(filtered_list)

# Factorial Calculation:
# Factorial formula: n!=n×(n−1)×(n−2)×...×2×1

# The ellipsis (...) indicates that the pattern continues, multiplying all the integers from n down to 1. It's a concise way to express the idea that you are multiplying a series of consecutive integers.
#For example, if n = 5, the expanded form of the factorial formula would be: 5! = 5 × 4 × 3 × 2 × 1
# Write a function that calculates the factorial of a given number. The factorial of a non-negative integer "n" is the product of all positive integers less than or equal to "n".

def calculate_factorial(n):
    factorial_result = 1
    for i in range(1, n + 1):
        factorial_result *= i
    return factorial_result
# Example usage
while True:
    user_input = input("Enter a number: ")
    if user_input.lower() == "exit":
        break
    try:
        user_num = int(user_input)
        factorial_of_num = calculate_factorial(user_num)
        print(f"The factorial of {user_num} is {factorial_of_num}")
        print("Type 'exit' to quit")
    except ValueError:
        print("Invalid input")

# Palindrome Checker:
# Write a function that checks if a given string is a palindrome (READS THE SAME BACKWARDS AS FORWARD).

def is_palindrome(user_input):
    if user_input.lower() == 'exit':
        return False  # Indicate exit condition
    elif user_input == user_input[::-1]:
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")
    return True  # Continue loop

# Example usage
while is_palindrome(input("Enter string (type 'exit' to stop): ")):
    pass

