# Defining functions
# Function syntax and parameters
# Return values
# Lambda functions

# Functions in python are defined using the def keyword followed by a function name and then paranteses(),
# inside the paranteses, you can put a parameter name and the colon.

# Example 1

def multiply(a, b):
    return a*b

result = multiply(9,0)
print(result)

# Example 2
# Multiple return values
def get_coordinates():
    return 10,20

x,y = get_coordinates()
print(x,y)

# Exercise 1
# Define a function greet with a parameter name, set to guest, and print a message I am a software programmer
def greet():
    # print("I am " +guest+ " and I am a software programer")
    return "I am Arinda", "I am a software programmer"
    
# greet("Arinda")
res = greet()
print(res)

# What was needed
def greet(name = "Guest"):
    print(f"I am a software programmer, {name}")
    
greet()

# return multiple values
def get_name_and_position():
    name = 'Arinda Asiimwe, '
    position = 'Software programmer'
    return name, position
    
name , position = get_name_and_position()
print(name,position)

# Exercise 2: Return name and age
def get_name_and_age():
    name = 'Arinda Asiimwe, '
    age = 23
    return name, age
    
name , age = get_name_and_age()
print(name,age)

# Notes
"""
def: keyword to define a function
function_name: name of the function
parameters: optional arguments passed to the function
docstrings: optional describes the function purpose
return: optional returns a value from the function

"""

# syntax for defining a function
def function_name(parameters):
    """Docstring, optional"""
    # Function body
    return parameters


# Lambda functions
# Lambda functions are small anonymous functions defined using the lambda keyword
# They are restricted to a single expression

# Syntax for lambda functions
# lambda parameter: expression

# Example 3
# create a lambda function to add two numbers

add = lambda a, b: a+b
print(add(1,5))

# Example 4: Use cases of lambda function for sorting
coordinates = [(1,2), (2,3), (3,1), (5,0)]
coordinates.sort(key=lambda coordinate: coordinate[1])
print(coordinates)

# Map , Filter and Reduce
# Example 5: Get the squares of 1 to 5 using map 
num_squares = [1,2,3,4,5]

squares = list(map(lambda x: x**2, num_squares))
print(squares)

# Exercise 3
# Define a function to get user info that accepts arbitrary keyword arguments 
# and prints each key value pair

get_user_info = lambda info_dict: [print(f"{key}: {value}") for key, value in info_dict.items()]

user_info = {"name": "Arinda", "age": 23, "course": "BSSE"}
get_user_info(info_dict=user_info)

def get_user_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Example usage:
get_user_info(name="Asiimwe", age=30, city="Kampala")


# Example 6
# How to handle a **kwargs in functions
def arinda(a, b, **kwargs):
    print(f"a: {a}")
    print(f"b: {b}")
    
    for key, value in kwargs.items():
        print(f"{key}: {value}")

arinda(1,2, x=100, y=200, z=300, e="Asiimwe", j=2.89)