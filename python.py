# #writing my first program

# print("welcome to Gomycode")
# print("have a wonderful learning experience")
# print("with data science skill")

# print("------------")
# #introducing new line to our code '\n'
# print("welcome to Gomycode \n have a wonderful learning experience \n with data science skill")

# #input function
#input('please enter your desired string here')

# print('hello' + input("please enter your name"))
# print('welcome'+ input('please enter your destination'))

#string concatination; string concatnation is used to join two strings

#print("hello " + input("enter your name")+ " welcome to "+ input("please enter your destination"))

#print("welcome " + input("what is your username") + " from " + input("where do you live")) 

# #birth_date = input("what is your age")
# age = 2024 - int(birth_date)
# print(age)

# birth_date = int(input("what is your age"))
# age = 2024 - birth_date
# print(age)

#assigning and reassigning variables
# name ="bisi"
# name ="peter"
# print(name)

#assigning multiple values for a single variable
# num1= num2= num3= 10
# print (num1)
# print (num2)
# print(num3)

#to check type
# print(type(num1))

#string indexing
#print("the first character in statement is",statement[0])

# word='welcome to gomycode'
# print("the first character in of the word 'welcome to gomycode is", word[0])

# splitted_word=word.split(' ')
# print(splitted_word)
# print(splitted_word[-1])

#python strip
# print(word.strip())

#to find length
# print(len(word))

# #changing case
# print(word.upper())
# print(word.lower())
# print(word.capitalize())

#numbers manipulation
# print(round(8/3))

#introducing f string
# num1,num2=2,3
# print("num1 and num2 are ", num1,num2)
# print(f'num1 is {num1}, and num2 is {num2}')
# print(f'{num1} ^ {num2} is {num1**num2}')


# x='3.5'
# print(int(x))
# print(float(x))
# print(bool(x))

# A=35
# B= str(A)
# C=int(B[0]) + int(B[1])
# print(f'{B[0]} + {B[1]} ={C}')

# age=int(input("what is your age"))
# week=52 * age
# days=365 * age
# months=12 * age

# neww=52 * 90
# newd=365 * 90
# newm=12 * 90

# print(f"you have {newd-days} days {neww-week} weeks and {newm-months} months left")

# Create a variable called "number" and assign any integer value to it.
# Use an if-else statement to check if the number is even or odd. You can use the modulo operator (%), which returns the remainder of a division operation, 
# to check if the number is divisible by 2. If the remainder is 0, the number is even, otherwise it is odd.
# You can also use logical operator "and" to check if the number is divisible by 2 and greater than 10.
# You can use logical operator "or" to check if the number is either divisible by 2 or greater than 10.

# number=int(input('what is your number'))
# if number %2 == 0:
#     print(f'the number {number} is an even number')
# else:
#     if number %2 == 0 and number > 10:
#      print(f'the number {number} is an even number')
#     else:
#        if number %2 == 0 or number > 10: 
#           print(f'the number {number} is an even number')
#        else:
#           print(f'the number{number} is an odd number')


# Instructions :
# you will be building a program that generates a band name based on the city you grew up in and the name of your pet.
# To complete the project, you will need to use skills such as printing inputs, variables, new lines, string manipulation, and debugging.
# Example Output:

# Create a greeting for your program.
# Ask the user for the city that they grew up in.
# Ask the user for the name of a pet.
# Combine the name of their city and pet and show them their band name.
# Make sure the input cursor shows on a new line:

# name=input('what is your name')
# city=input('where did you grow up?')
# pet=input('whats the name of your pet') 

# print(f'welcome {name} \n your band name is {city+pet}')  



# Create a variable called "number" and assign any integer value to it.
# Use an if-else statement to check if the number is even or odd. You can use the modulo operator (%), which returns the remainder of a division operation, 
# to check if the number is divisible by 2. If the remainder is 0, the number is even, otherwise it is odd.
# You can also use logical operator "and" to check if the number is divisible by 2 and greater than 10.
# You can use logical operator "or" to check if the number is either divisible by 2 or greater than 10. 

# number=12
# if number %2==0:
#    print(f"the number {number} is an even number")
# else:
#    if number %2==0 and number >10:
#       print(f"the number {number} is an even number and is also greater than 10")
#    else:
#       if number %2==0 or number>10:
#          print(f"the number {number} is either even or the number {number} is greater than 10")


#write a program to detect prime number 

# number=int(input('what is your number'))
# if number %2 ==0:
#     print(f'this number {number} is a an even number')
# else:
#     print(f'this number {number} is an odd number') 

# DATA STRUCTURE IN PYTHON
# List,dictionary,tuple and set (DICTIONARY,KEY,VALUES,ITEMS).


##empty_list[]
#list_fruit=['apple','orange','banana','watermelon','guava']
#list_fruit[2:4] will print banana and watermelon because in string slicing the first will the called but the second will only be called if you add one to it.
#print(list_fruit[-1:])
# print(list_fruit[3:])

#LIST APPEND
# list_fruit.append('mango')
# print(list_fruit)

#LIST INSERT
# list_fruit.insert(2,'cherry')
# print(list_fruit)

# list_fruit[4]='pear'
# print(list_fruit)

# #LIST REMOVE
# list_fruit.remove('apple')
# print(list_fruit)

# del(list_fruit[3])
# print(list_fruit)

#dictionary
#dict_item={'name':'awwal','course':'data science','year':2024}
# for key in dict_item.keys():
#     print(key)

# for val in dict_item.values():
#     print(val)

# for item in dict_item.items():
#     print(item)


#DICT UPDATE
#dict_item.update({'session':'morning'})
# print(dict_item)


# #dict delete
# dict_item.pop('year')
# print(dict_item)
# del(dict_item['course'])

#to rename keys
# dict_item['student name']=dict_item.pop('name')
# print(dict_item)

#to change values
# dict_item['cohort']=2

# sample_dic={'name':['awwal','bisi','emma','soji','ruth','tobi'],'course':['D5','CS','FS','SD','UI/UX','DA'],'year':[2024,2023,2024,2024,2023,2024]}
# # for key in sample_dic.keys():
# #     print(key)

# #     for val in sample_dic.values():
# #         print(val)

# #         for items in sample_dic.items():
# #             print(items)


# # sample_dic.update({'country':['france','germany','russia','ghana','mexico','america'})
# # print(sample_dic)

# # sample_dic.pop('course')
# # print(sample_dic)


# # sample_dic['firstname']=sample_dic.pop('name')
# # print(sample_dic)


# # Instructions :
# # Tuples:

# # Create a tuple called "person" that contains a string "John" as a name, 25 as an age and "male" as a gender.
# # Print the name of the person
# # Try to change the age of the person and see what happens.
# # Lists:
# # Create a list called "grocery_list" that contains "milk", "bread", "eggs", "bananas"
# # Print the first item in the grocery_list.
# # Add "chocolate" to the grocery_list
# # Remove "milk" from the grocery_list
# # Sets:
# # Create a set called "unique_numbers" that contains the integers 1, 2, 3, 4, 5
# # Add number 6 to the unique_numbers
# # Print the length of the unique_numbers
# # Try to add a duplicate number and see what happens
# # Dictionaries:
# # Create a dictionary called "employee" that contains the keys "name", "age", "position" and "salary", with their corresponding values "John", 25, "Developer" and 3000 respectively.
# # Print the employee's name
# # Change the employee's position to "Manager"
# # Add a new key "email" with the value "john@example.com" to the employee dictionary


# # grocery_list=['milk','bread','eggs','bananas']
# # print(grocery_list[0])

# # grocery_list.append('chocolate')
# # print(grocery_list)

# # grocery_list.remove('milk')
# # print(grocery_list)

# # unique_numbers={1,2,3,4,5}
# # unique_numbers.add(6)
# # unique_numbers.add(3)

# # employee={'name':'john','age':25,'position':'developer','salary':3000}
# # print(employee['name'])


# # employee['position']='manager'
# # print(employee)

# # employee.update({'email':'john@example.com'})
       


# #LOOP
# # string='welcome to Gomycode'
# # for letter in string:
# #     print('the letter is',letter)


# for num in range(10,21):
#     print(num)

# for num in range(10,21,2):
#     print(num)

# for num in range(10,21):
#     if num %2 == 0:
#         print(num)


# for num in range(10,21):
#     if num %2 != 0:
#         print(num)

# #for loop with list and enumerate
# list1=['mango','orange','lemon']
# for index,fruit in enumereate(list):
#     print(f'index {index} item of the list is {fruit}')



# student_scores =[78,65,89,86,55,91,64,89,100]
# highest_score=student_scores[0]
# for score in (student_scores):
#     if score > highest_score:
#         highest_score=score
# print(highest_score)


# import random
# from random import randint
# random_num = randint(0,1)
# if random_num==0:
#     print('tail')
# else:
#     print('head')


# loop,random

#WHILE LOOP AND FOR LOOP

# list_fruit=['apple','orange','banana','watermelon','guava']

# i=0
# while i < 10: #this is the number of iterations if condition is true
#     print(f"the value of i is {i}") 
#     if i > 5:
#         print(i)
#     i += 1


#continue running a set of task until the condition of a "while" is met

#while <condition>: #while condition to meet or to check
    #<task>#task to repeat until the while condition is met

   
# i= 2
# if i > 5:
#     print('yes')  
# else:
#     print('no')  
    


# list_fruit=['apple','orange','banana','watermelon','guava']

#print(list_fruit[4])
# print(len(list_fruit))

# i=0

# while i < len(list_fruit):
#     #print(f"I am i and my value is {i}, I respresent the list index")
#     #print (list_fruit[i])
#     if list_fruit[i] == "banana":
#         print("Yes Banana")
#     else:
#         ...
#         #print("No Banana")
        
#     i += 1


# for i in list_fruit:
#     if i == "cherry":
#         print("Yes Banana")
#     else:print("no shit")


# if "banana" in list_fruit:
#     print("yes")
# else:
#     print("no")

# 

#LAMBDA

#lamda map
# num_list=[12,13,45,67,20,100]
# square_num=list(map(lambda num: num **2,num_list))
# print(square_num)


# #lambda reduce
# from functools import reduce
# sum_reduce((lambda num1,num2: num1 + num2))

# list=[1,2,3,4,6,7,8]
# valv=0
# def miss():
#     if valv = 5

INHERITANCE

class player():
    def __init__(self,name,age,hp):
        self.name=name
        self.age=age
        self.hp=hp
    def take_damage(self,damage):
        return f'{self.name},{self.hp},{damage},{self.hp-damage}'
    
player1=player('tobi',21,120)
print( player1.take_damage(20))


# child class

class features_player(player):
    def __init__ (self,name,age,hp):
        super(). __init__(name,age,hp)
    def salary(self,amount):
        self.amount=amount
        return f'{self.amount*self.hp}'
    
player1=features_player('soji',26,100)
print(player1.take_damage(20))
print(player.salary(2))


#polymorphism

class Animal:
    def __init__(self,name,animal_class):
        self.name=name
        self.a_class=animal_class
        def display(self):
            return f'the animal class is {self.a_class} and the name is {self.name} '
        
class Mammal(Animal):
    def __init__(self, name, animal_class,reproduction):
        self.reproduce=reproduction
        super().__init__(name, animal_class)
    def display(self):
        return f'The animal class is {self.a_class},the name is {self.name} and it reproduce by {self.reproduce}'
    
class Bird(Animal)
    def __init__(self, name, animal_class,fly):
        self.fly=fly
        super().__init__(name, animal_class)
    def display(self):
        return f'the animal class is {self.a_class},the name is {self.name} and it can {self.fly}'
    

Animal1=Mammal('goat','mammal','birth')
Animal2=Bird('sparrow','bird','fly')
animal_p=Animal('lion','wild')
animal_list=[Animal1,Animal2,animal_p]
for animal in animal_list:
    print(animal.display())



# import math

# class shape:
#     def area(self):
#         pass

# class circle(shape):
#     def __init__(self,radius):
#         self.radius=radius
#         def area(self):
#             return f'{math.pi*self.radius**2}'
# class rectangle(shape):
#     def __init__(self,length,breath)
#         self.l=length
#         self.b=breath
#     def area(self):
#         return f'{self.l * self.b}'
# class triangle(shape)
#     def __init__(self,base,height)
#         self.b=base
#         self.h=height
#     def area(self)
#         return f'{0.5*self.b*self.h}'
    
# circle=circle(5)
# rectangle=rectangle(4,6)
# triangle=triangle(3,5)
# shape_l=[circle,rectangle,triangle]
# for sh in shape_l:
#     print(sh.area())


# #write a class that contain member list in their 
# respective group make sure the group has assign leader


class economics():
    def __init__(self,name,name2,name3):
        self.name=name
        self.name2=name2
        self.name3=name3
    def department(self):
        return f'the economics department students are {self.name},{self.name2},{self.name3}'
    
class science(economics):
    def __init__(self, name, name2, name3,leader):
        self.leader=leader
        super().__init__(name, name2, name3)
    def department(self):
        return f'the science department leader is {self.leader} and the students are {self.name},{self.name2},{self.name3}'
    
school1=economics('soji','tobi','ruth')
school2=science('bisi','kaffy','lawal','emmanuel')
school_list=[school1,school2]
for s in school_list:
     print(s.department())

    
    
class Economics:
    def __init__(self, name, name2, name3):
        self.name = name
        self.name2 = name2
        self.name3 = name3

    def department(self):
        return f'the economics department students are {self.name},{self.name2},{self.name3}'


class Science(Economics):
    def __init__(self, name, name2, name3, leader):
        super().__init__(name, name2, name3)
        self.leader = leader

    def department(self):
        return f'the science department leader is {self.leader} and the students are {self.name},{self.name2},{self.name3}'


school1 = Economics('soji', 'tobi', 'ruth')
school2 = Science('bisi', 'kaffy', 'lawal', 'emmanuel')
school_list = [school1, school2]

for s in school_list:
    print(s.department())

st_ = Science('n', 'y', 'q', 'j')
print(st_.department())
    