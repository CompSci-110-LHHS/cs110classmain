################ Python If...Else, If...Elif...Else Statements #################

#Python programs can branch based on whether the outcome a condition is 'True' or 'False'
#If...Else statements are used to define the two different outcomes, for example:

#Take a user input in a number guessing game:
################ EXAMPLE 1 - Start ##################

print("Guess a number between 1 and 10: ", end="")     #Remember print defaults to a new line, so added end = "" lets us write respone on same line
guessNum = input()
numToGuess = 6

if guessNum == numToGuess:
    print("Wow! You guessed write")
else:
    print("Sorry, game over!")

################ EXAMPLE 1 - End ##################
    


#If we want to give the user more feedback, we can evaluate more conditions using the else if block:
################ EXAMPLE 2 - Start ##################

# print("Guess a number between 1 and 10: ", end="")    
# guessNum = input()
# numToGuess = 6

# if guessNum == numToGuess:
#     print("Wow! You guessed write")
# elif guessNum > numToGuess:
#     print("Too High, game over!")
# elif guessNum < numToGuess:
#     print("Too Low, game over!")
# else:
#     print("Sorry, game over")

################ EXAMPLE 2 - End ##################
    
    

#We can nest If...Else statements too. For example, we should check if the user entered and int value before evaluating first
################ EXAMPLE 3 - Start ##################
        
# print("Guess a number between 1 and 10: ", end="")    
# guessNum = input()
# numToGuess = 6

# if type(guessNum) == int:
#     if guessNum == numToGuess:
#         print("Wow! You guessed write")
#     elif guessNum > numToGuess:
#         print("Too High, game over!")
#     elif guessNum < numToGuess:
#         print("Too Low, game over!")
# else:
#     print("Sorry, not a number...game over")

################ EXAMPLE 3 - End ##################

    