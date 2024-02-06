#Once a string is defined, we can use built-in methods (aka functions) to perform many types of operations
myString = "String Example"
print(myString)

#Returns the length of a string
strLength = len(myString)
print(strLength)

#Pick a character or range of characters from String
print(myString[2]) #single letter 'r'
print(myString[2:5]) #range from "rin" not including index 5

#Strings are 'immutable' python objects, they cannot be modified like lists. For Example, uncomment to see error
#myString[1] = "P" #Does not evaluate to "Ptring Example"

#Matching Patterns in string
exampleTxt = "I am the one who knocks"
print("knocks" in exampleTxt) #Is True
print("knocks" not in exampleTxt) #Is False

#Changing the case using uppercase() and lowercase() methods
print(exampleTxt.upper())
print(exampleTxt.lower())

#Removing whitespace
whitespaceTxt = " White space is annoying!   "
print(whitespaceTxt.strip())

# There are lots of other methods for working with strings, here are some useful ones I use a lot
# count(), find(), index(), replace(), see slides for definitions and uses
