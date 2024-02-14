################ Python Strings - Formatting #################

#Define a string variable using quotations 
myName = "Jeff"
myRole = "Teacher"
mySchool = "Leo Hayes High School"

print(myName)
print(myRole)
print(mySchool)

#Add Strings together with the '+' operator
print(myName + " is a " + myRole + " at " + mySchool)

#Formating Strings using f-string syntax
print(f"{myName} is a {myRole} at {mySchool}")

#CHALLENGE: Rewrite the above to create a sentence that discribes you and your role at LHHS
#
# Add Your Code HERE
#

#Formating Strings using format() method
item1 = "apples"
item2 = "oranges"
item3 = "pineapple"

groceryList = "Pick up six {}, six {} and one {}".format(item1, item2, item3)
print(groceryList)

groceryList2 = "Pick up six {0}, one {2} and six {1}".format(item1, item2, item3)
print(groceryList2)

#CHALLENGE: Rewrite the above to create a sentence that discribes a list of your favorite shows, hobbies etc...
#
# Add Your Code HERE
#

#Using special characters such as 'quotes' within quotes - using 'escape characters'
movieQuote = "You know what they call a \"Quarter Pounder with Cheese\" in Paris?"
print(movieQuote)

#See slides for more escape character examples

#Food for thought, what is the difference between these two variables and how could you check?
myAge1 = 38
myAge2 = "38"



