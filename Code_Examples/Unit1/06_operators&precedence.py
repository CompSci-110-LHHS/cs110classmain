################ Python Operator & Operation Precedence #################

#comparison operators: A few examples
a = 6
b = 4
c = 6

#Equal ==
#Not Equal !=
#Great Than >
#Greater or equal than >=
#Lesser Than <
#Lesser or equal than <=

#Here are some examples using the above variable values:
a == b #FALSE
a != b #TRUE
a > b #TRUE
a >= b #TRUE
a <= c #TRUE

#CHALLENGE: Try printing these comparison to see the answer in the terminal

#logic operators: evaluate conditions
    # and -- TRUE if both conditions are true
    # or -- TRUE if either conditions are true
    # not -- flips the result TRUE -> FALSE or vice versa

a > b and a == c # TRUE
a > b or a < c # TRUE
not(a > b and a == c) #FALSE

#Precedence is the order of operations arithmetic operators are executed, think math class
#1 - Parentheses -- ()	
#2 - Exponentiation -- **		
#3 - Multiplication, division, floor division, and modulus -- *  /  //  %		
#4 - Addition and subtraction -- +  -	

#CHALLENGE: What does the following equation evaluate to?
x = 6
a = 10

y = (x+6) + 3 * (4*a + 10)**2