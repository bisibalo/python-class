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

name=input('what is your name')
city=input('where did you grow up?')
pet=input('whats the name of your pet') 

print(f'welcome {name} \n your band name is {city+pet}')  







