import math


################## UNIT 1 Skill Test - PART II #####################

#Section A: Practice with Numbers, operators and Precedence

#Q: Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn



#Q: Write a Python program to test whether a number is a prime (i.e. divisable by only 1 and itself)
#HINT: Use the modulus operator and a for loop:

##ANSWER##
n = int(input("Input a number to check: "))
prime = True

for i in range(1,n):  
    remainder = n % i
    if remainder == 0 and i != 1 and i != n:
        print("not a prime")
        prime = False
        break

if prime != False:
    print(f"{n} is a prime number")
    #use an if...else statement here

#Q - DONE: Write a python program that calculates the volume and area of a sphere with the following data
# radius = 2.4

# Volume of sphere V = 4/3*pi*r^3 
# Area = 4*pi*r^2

##ANSWER##
radius = 2.4
pi = math.pi
Volume = 4/3*pi*radius**3 
Area = 4*pi*radius**2

#Section B: Practice with Strings

#Section C: Practice with Booleans

#Section D: List, Dictionaries and Tuples

#Q2: Write a Python program to display the first and last colors from the following list.

color_list = ["Red","Green","White" ,"Black"]

#Q1: Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.

