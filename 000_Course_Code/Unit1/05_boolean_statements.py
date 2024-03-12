################ Python Booleans - True or False Values #################

#The following statements evaluate to either true or false and can be printed to the terminal:
print(4 > 3) #TRUE
print(2 < 1) #FALSE
print(10 == 5) #FALSE



#When combined with if statements, booleans become a part of programming logic
password = "123password" 
pwdLength = len(password) #returns the length of the string

if pwdLength > 12:         #evaluates to FALSE   
    print("Great, your password is strong!")
else:
   print("Sorry, password is too weak. Try again!")



#The bool() method evaluates the TRUTHY or FALSEY-ness of a statement
print(bool("Hello")) #TRUE
print(bool(12)) #TRUE
print(bool(0)) #FALSE

#MOST EMPTY VALUES ARE FALSEY
bool(False)
bool(None)
bool(0)
bool("")
bool([])
bool({})
bool(())

#Consider the IF statement
if "Hello": #evaluates to TRUE   
    print("evaluates to TRUE!")


#Returning TRUE or FALSE from a Function and performing and IF...Else Statement
def returnsTrue() :
  return True

if returnsTrue():
  print("YES!")
else:
  print("NO!")

#CHALLENGE: Write a function like above called returnsFalse(), the will result in "NO!" being printed
  


