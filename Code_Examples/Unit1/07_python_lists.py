
################ Python Lists #################

# List: ordered and changeable. Allows duplicate members.
# Lists are a collection of data stored as a single variable of any size, any data type. All values are indexed, iterable and mutable (i.e. changable)

#Here are some examples:
myGroceryList = ["apples", "oranges", "pinapple", "grapes"]
systemStatus = [True, True, False, True]
mixedValues = [True, "LHHS", 27, 13.57]

print(myGroceryList)  #This outputs: ["apples", "oranges", "pinapple", "grapes"]

#len() method exists to determine length of the list
print(len(myGroceryList))
#CHALLENGE: print the length of systemStatus and mixedValues

#Accessing a specic value(s) via indexing (or negative indexing)
print(systemStatus[2])
print(systemStatus[-1])  #Both return False
print(mixedValues[:3])   #prints [True, "LHHS", 27], Negative ranges can also be used
#CHALLENGE: Use negative ranges to select items from above list

#Searching for value using the 'in' operator
if False in systemStatus:
    print("There is an error! Attention required")
else:
    print("All systems green! Coffee break")

#Several list methods exist that are useful:
    
    # append()	Adds an element at the end of the list
    # extend()	Add the elements of a list (or any iterable), to the end of the current list
    # insert()	Adds an element at the specified index
    # remove()	Removes the item given value
    # pop()	    Removes item at specified position    
    # clear()	Removes all items from the list    
    # copy()	Returns a copy of the list
    # index()	Returns the index of the first element with the specified value
    # count()	Returns the number of elements with the specified value
    # reverse()	Reverses the order of the list
    # sort()	Sorts the list    

#Combining with strings
indexVal = systemStatus.index(False)
print(f"There is a problem in reactor: {indexVal + 1}. Status reads: {systemStatus[indexVal]}")

#Values can be changed
systemStatus[2] = True
print(systemStatus[2]) #False replaced with True

#Lists are iterable - they can be looped over
for x in systemStatus:
    if x == True:
        status = "Online"
    else: 
        status = "Offline"
    print(f"Reactor is: {status}")

#Nesting Lists:
list1 = ["lions", "tigers", "bears"]
list2 = ["kittens", "puppies", "fluffy bunnies"]

myPets = [list1, list2]
print(myPets)  #Outputs: [["lions", "tigers", "bears"],["kittens", "puppies", "fluffy bunnies"]]

#To print a specific value, we need to index twice into each layer of the nested list like this:
myFavoritePet = myPets[1][2]
print(myFavoritePet) #Outputs: fluffy bunnies


    


