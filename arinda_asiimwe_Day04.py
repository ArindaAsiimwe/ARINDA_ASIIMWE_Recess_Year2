# Dictionaries
# Creating and using dictionaries
# Dictionary methods and operations
"""
Dictionaries in pyrhon are collections of keys and values
-Can be unordered
-Are mutable 
-Can be indexed by keys
"""

# Example 1: Create a dictionary for a student pursuing BSSE,
# the key must be your name, age, technology interest, course and year of study.
# Put your own details

student_dict = {
    'name': 'Arinda',
    'age' : 23,
    'technology': 'AI',
    'course': 'BSSE',
    'year': 'Year 3'
}

print(student_dict['name'])

# Exercise 1
# Modify age and technology
student_dict['age'] = 45
student_dict['technology'] = 'Machine learning'

print(student_dict)

# Example 2: adding keys and values
student_dict['email'] = 'aritah185@gmail.com'

print(student_dict)

# Exercise 2
student_dict.popitem() #it removes the last item of the dictionary
# student_dict.pop('name') # removes the specified key and its value
print(student_dict)
del student_dict['course']
print(student_dict)


# Example 3
# Common Dictionary methods
"""
get() // returns the value for the specified key if the key is in the dictionary
if not it returns the default value

update() // Updates the dictionary with the elements from another dictionary

pop() // Removes the specified key and return the corresponding value
"""
# Example 3: Use the get method to get the value

print(student_dict.get('technology'))

# Exercise 3: Use the update method to change value in age 

student_dict.update({'age': 23})
print(student_dict)


# Exercise 4: Use the if to check if the key 'age' is present in the dictionary

if 'age' in student_dict:
    print(" age is present in the dictionary.", student_dict['age'])
    
else:
    print(" age is not present in the dictionary.")
    

# Example 4
# keys(), values() and the items() methods
print(student_dict.keys())
print(student_dict.values())
print(student_dict.items())

"""
keys() returns a view of objects that displays a list of all keys
values() returns a view of objects that displays a list of all values
items() returns a view of objects that displays a list of dictionary keys and
values tuple pairs

 """
 
 # Exercise 5: Use the update method to change the course and add a new 
 # key "WhatsApp_Number" to the dictionary
 
student_dict.update({
    'course': 'BSC',
    'WhatsApp_Number': '0702285073'
})
print(student_dict)

