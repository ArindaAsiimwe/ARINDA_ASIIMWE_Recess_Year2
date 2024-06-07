# if, elif, else

# Example 1
age = 70

if age > 18:
    print("You are an adult")
elif age > 65:
    print("You are a senior citizen")
else:
    print("You are a youth")
    

# Example 2
grade = 45

if grade >=90:
    print('Excellent')
elif grade >=80:
    print('Very good')
elif grade >=70:
    print('Good')
else:
    print('Not good')
    
# Exercise 1 in class

age = int(input('Enter your age please: '))

if age < 13:
    print('Discount is UGX 1,000')
elif age>=13 and age<18:
    print('Discount is UGX 500')
elif age>=18 and age<=65  :
    print('No discount, pay full price of UGX 2000')
else:
    print('Pay UGX 5000')
    
    
# LOOPS

# for loop(lists, tuples, dictionary, set, string)

# while repeats as long as a condition is true

# Example 3 

cars = ['Tesla', 'Audi','BMW', 'Jeep', 'RangeRover']

for car in cars:
    print(car)
    
# Example 4 count 1 to 10

count = 1
while count <=10:
    print("Count 1 to 10:", count)
    count += 1
    
# Exercise 2

# 1
colors = ['Indigo', 'Turqoise', 'Cyan', 'Green']

reverse = colors[::-1]
print('My favorite colors are' )
for color in colors:
    print(color)
# for reverse in for loop 
for color in reverse:
    print(color)
    
# 2 
list = [1,2,3,4,5]
index = len(list)-1
while index>=0:
    print(list[index])
    index -= 1
    
   




    
    
    

