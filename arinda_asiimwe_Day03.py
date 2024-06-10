"""
Python best practices
Follow PEP 8

1. Indentation
2. Maximum line length
3. Blank lines
4. Meaningful names
5. Use list comprehesions
"""
# Use meaningful names
def calculate_area(r):
    pass

total_price = 1000

# Python operators
"""
Python operators
 
Name of operator            Symbol with example
Addition                        x + y
Subtraction                     x - y
Multiplication                  x * y
Division                        x / y
Modulus                         x % y
Exponent                        x ** y
Floor division                  x // y

# Comparison operators
Name of operator            Symbol with example
Equal                           x == y
Not wqual                       x != y
Greater than                    x > y
Less than                       x < y
Greater than or equal to        x >= y
Less than or equal to           x <= y

# Logical operators
Name of operator            Symbol 
and                             and 
or                              or 
not                             not

# Membership operators
Name of operator            Symbol with example
in                              x in y
not in                          x not in y

# Bitwise operators
Name of operator            Symbol with example
Bitwise AND                   &
Bitwise OR                    |
Bitwise XOR (exclusive OR)    ^
Bitwise NOT (complement)      ~
Left Shift                    <<
Right Shift                   >>

# Python cases
1. snake_case
2. camelCase
3. PascalCase
4. UPPERCASE
5. kebab-case
"""

# Comprehesions (Lists, dictionary comprehesions)
"""
Comprehesions provide a concise way to create lists and 
dictionaries
lists           [] square brackets used to store multiple items in a single variable
dictionary      {} curly braces used to store data values in key:value pairs
"""

# Example 1 basic list comprehesion
# create a list of squares in range of 10
list_of_squares= [x**2 for x in range(10)]
print(list_of_squares)

# Exercise 1
# create a list of even squares in the range of 20
list_of_even_squares = [x**2 for x in range(20) if x%2==0 ]
print(list_of_even_squares)

# Example 2 dictionary comprehesion
# create a dictionary comprehesion for my favorute cars and count the length of characters
favorite_cars = ['Lexus','Jeep','Hammer']
car_lengths = {car: len(car) for car in favorite_cars}
print(car_lengths)

# Exercise 2
# create a list of tuples where each tuple contains a 
# number and its cube, for numbers between 1 and 10 
# using dictinary comprehesion

cubes = {number: number**3 for number in range(1,11)}

cubes_tuple = tuple(cubes.items())
print(cubes_tuple)

