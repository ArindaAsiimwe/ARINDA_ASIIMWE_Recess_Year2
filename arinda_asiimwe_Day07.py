#Inheritance and polymorphism
"""
Inheritance and method overriding
polymorphism and method resolution order
Abstract classes and interfaces
"""

# Inheritance and method overriding
"""
Inheritance and method overriding allows a class(child class) to inherit atttributes and methods
from another class(parent class)

key concepts
?Base class(parent class): Class whose properties are inheriteed by another class
Derive class(child class): Class that inherits 
"""

# example 1: Syntax
# create a class where a dog inherits from animal and overrides with a speak method
 
print('Inheritance')
class Animal:
    def speak(self):
        return 'Animal is making a sound'

class Dog(Animal):
    def speak(self):
        return 'Barking'
    
# Implementation of inherited classes
animal = Animal()
dog = Dog()

print(animal.speak())
print(dog.speak())

# Polymorphosim
# It allows objects of different classes to be treated as objects of a common superclass.
# Method resolution odrer(MRO): is the order in which python looks for aa method in a hierachy classes.

# Example 2
# How polymorphism works in python

class Animal:
    def speak(self):
        return "Animal speaks"

class Dog(Animal):
    def speak(self):
        return "Barks"
    
class Cat(Animal):
    def speak (self):
        return "Meowww"
    
def make_animal_speak(animal):
    print(animal.speak())

print('\n')
print('Poymorphism')
make_animal_speak(Dog())
make_animal_speak(Cat())




"""
# Exercise 1: Create a simple application to manage different types of vehicles. 
# Implement derived class to demonstrate inheritance and polymorphism

Requirements
1. Base class to vehicle
Attributes: make, model and year
Methods: display_info()

2. Derived classes
Car: inherit from vehicle
attributes: number_of_doors
overrides: display_info()

Motorcycle: inherit from vehicle
attributes: type_of_bike(cruiser, sport, touring)
overrides: display_info()

# Exercise 2: Polymorphism
# Create a function that accepts a list of vehicle objects and call their display_info()
# method to print details of each vehicle
"""
print('\n')
# Solution 1(Inheritance)
class Vehicle():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year =year
    
    def display_info(self):
        print(f"Vehicle Info: {self.year} {self.make} {self.model}")

class Car(Vehicle):
    def __init__(self, make, model, year, number_of_doors):
        super().__init__(make, model, year)
        self.number_of_doors = number_of_doors
        
    def display_info(self):
        print(f"Car Info: {self.year} {self.make} {self.model}, Doors: {self.number_of_doors}")


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, type_of_bike):
        super().__init__(make, model, year)
        self.type_of_bike = type_of_bike
        
    def display_info(self):
        print(f"Motorcycle Info:  {self.make} {self.model} {self.year}, Type: {self.type_of_bike}")


car1 = Car("Toyota", "Honda", 2020, 4)
motorcycle1 = Motorcycle("Harley-Davidson", "Street 750", 2019, "Cruiser")

car1.display_info()
motorcycle1.display_info()

# Polymorphism
# Solution 2
def display_vehicle_info(vehicles):
    for vehicle in vehicles:
        vehicle.display_info()

vehicles = [car1, motorcycle1]
display_vehicle_info(vehicles)

print('\n')


# Reading and writing files in Python
"""
1. Working with text files

Hnadling CSV files
JSON and XML file processing


"""
# 1. Working with text files, open, read, write and close
# Note: Pthon provides inbuilt functions to handle text files

# key concepts
"""
The functions provided by python
Opening file: open() 
Reading file: read()
Writing file: write()
Close file:   close()

"""

# Example 3: Write a file and read a file

# writing to a text file
with open('arinda.txt' , 'w') as file:
    file.write('I am Arinda, and I love programming\n')
    file.write('I like using stack overflow')

print('Text file created successfully')

# reading from a text file
with open('arinda.txt', 'r' ) as file:
    content = file.read()
    print(content)

print('The data from the text file read successfully')

print('\n')    


# Handling CSV files
"""
CSV(Comma Seperated Values) file widely used for data exchange

Key concepts:
Read CSV files: Using 'csv.reader()'
Write to CSV files: Using 'csv.writer()'
DictReader and DictWriter: The class read and write CSV files as dictionaries
"""

# Example 4: Writing and Reading CSV files

import csv

# Writing to a Csv file
with open('arinda.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Name: ', 'Position: ','Course: '])
    writer.writerow(['ArindaAsiimwe', 'Student', 'BSSE'])
    writer.writerow(['Hillal ', 'Student', 'Bse'])
    
print('CSV file created successfully')
    
with open('arinda.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        print(row)
        
print('Data from the text file read successfully')
print('\n')


# JSON and XML file processing
"""
JSON(JavaScript Object Notation) and XML(eXtensible Markup Language)
These are formats used to structure data

Key concepts
Loading JSON data: using json.load() for reading JSON file
dumping JSON data:Using json.dump() for writing JSON file
parsing JSON data: using json.loads() for handling JSON strings
"""

# Example 5: write and read JSON File
import json
# writing to a JSON file
student_data = {
    'Name':'Arinda',
    'Course':'BSSE',
    'Year':'3'
}

# open the file
with open('student_data.json','w') as json_file:
    json.dump(student_data,json_file) 

print('The JSON created successfully')

# reading the JSON file
with open('student_data.json', 'r') as json_file:
    student_data = json.load(json_file)
    print(student_data)
    print('The data read successfully')

print('\n')



# Exercise 2: Write and read an xml file
import xml.etree.ElementTree as ET

# Data to be written to the XML file
student_data = {
    'Name': 'Arinda',
    'Course': 'BSSE',
    'Year': '3'
}

# Writing to an XML file
root = ET.Element("student")
for key, value in student_data.items():
    element = ET.SubElement(root, key)
    element.text = value

tree = ET.ElementTree(root)
tree.write("student_data.xml")

print("XML file 'student_data.xml' created successfully.")

# Reading from an XML file
tree = ET.parse('student_data.xml')
root = tree.getroot()

student_data = {}
for child in root:
    student_data[child.tag] = child.text

print(student_data)
print('Data from the XML file read successfully')
print('\n')


print('Abstraction')
# Exercise 3: Using abstraction calculate the area and perimeter of a rectangle
from abc import ABC, abstractmethod

class Shapes(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass

class Rectangle(Shapes):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

rect = Rectangle(5, 3)
print(f"The area of the rectangle is: {rect.calculate_area()}")
print(f"The perimeter of the rectangle is: {rect.calculate_perimeter()}")

