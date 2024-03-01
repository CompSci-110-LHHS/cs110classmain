################# Python Methods ###################


################ EXAMPLE 1 - Start ##################

#Methods (or Functions) allow pieces of code to be reused
#when a repetitive task is defined. Pseudo code might help
#plan your programs actions:

#Should I bring an umbrella?
#If raining, Yes Bring Umbrella
#Else, No
#Start walking to school
#If raining, Yes go back and get one
#Else continue on
#Go classes until days end
#If raining, Yes get from locker
#Else continue on

#Functions
def getUmbrella(weather):
    if weather == "True":
        print("Get an umbrella!")
    else: 
        print("Nah, we're good. Leave it")

#Start of Program
print("--------------------------------")
print("Another new day! Let's get ready!\nShould I bring and umbrella?")
print("--------------------------------")
weather = input("Is it Raining? (True/False): ")
getUmbrella(weather)

print("Walking to School, Lets check the weather again...")
weather = input("Is it Raining? (True/False): ")
getUmbrella(weather)

################ EXAMPLE 1 - END ##################
