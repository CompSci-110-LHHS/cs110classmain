################ Python For Loops #################

#For loops repeat for a defined number of times. Syntax looks like this:

# for x in range(start, end, increament):
#     code that runs end of range is reached
#     default start is 0

#Here is a basic examples
################ EXAMPLE 1 - Start ##################


for a in range(0, 10, 2):
    print(f"{a} ", end="")   #OUTPUT = 0 2 4 6 8, even numbers
    
################ EXAMPLE 1 - Start ##################
    

#For loops can be used to loop of list, dictionaries and tuples as we've seen
################ EXAMPLE 2 - Start ##################
myGroceryList = ["apples", "oranges", "pinapple", "grapes"]

for item in myGroceryList:
    print(f"Remember to buy: {item}") 
    
################ EXAMPLE 2 - Start ##################
    
#For loops can nested, this examples draws some ascii art
################ EXAMPLE 3 - Start ##################
sideA = 8
sideB = 8

for i in range(0, sideA):
    for j in range(0, sideB):
        print("* ", end="")
    print()
        
################ EXAMPLE 3 - End ##################
    
