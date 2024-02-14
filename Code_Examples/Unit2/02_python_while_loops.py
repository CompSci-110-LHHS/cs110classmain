################ Python While Loops #################

#Take the number guessing game from If...Else code example. We can allow multiple guesses using 
#While loops

#While loops continuously run as long as its condition evaluates to 'True'. Syntax looks like this:

# while (condition):
#     code that runs while true


################ EXAMPLE 1 - Start ##################
statusCode = 0 #Initialize a status variable to zero so while starts in the true condition and runs at least once

while statusCode == 0:        
    print("Guess a number between 1 and 10: ", end="")    
    guessNum = input()
    numToGuess = 6

    if guessNum.isdigit():
        guessNum = int(guessNum) #type casting str to int
        if guessNum == numToGuess:
            print("Wow! You guessed write")
            statusCode = 1 #end loop
        elif guessNum > numToGuess:
            print("Too High, try again!")
            statusCode = 0 #run loop again
        elif guessNum < numToGuess:
            print("Too Low, try again!")
            statusCode = 0 #run loop again
    else:
        print("Sorry, not a number...try again")

################ EXAMPLE 1 - End ##################
        
#Two key words seen with loops are 'break' - breaks out of the loop completly and 'continue'-skips to the next iteration. Lets look at an example:

#This example breaks out of the loop once i = 5 and doesn't continue counting to 10
################ EXAMPLE 2 - Start ##################

# i = 0 #initialize counting variable as zero

# while i <=10:
#     i += 1
#     if i == 5:
#         break
#     else:
#         print(i)
        

################ EXAMPLE 2 - End ##################
        
#This example continues to the next loop iteration once i = 5 and doesn't print the value of i
################ EXAMPLE 3 - Start ##################

# i = 0 #initialize counting variable as zero

# while i <=10:
#     i += 1
#     if i == 5:
#         continue
#     else:
#         print(i)        

################ EXAMPLE 3 - End ##################