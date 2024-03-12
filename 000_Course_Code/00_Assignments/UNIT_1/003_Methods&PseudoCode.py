############################################################
################ UNIT 2: Python Methods ####################
################## Practice With Methods####################
############################################################

#Methods (or Functions) allow pieces of code to be reused
#when a repetitive task is defined. Pseudo code might help
#plan your programs actions:

#Q: Assignment: Break down an everyday task into a “program” of at least five or six procedures. Try to use Methods when tasks are repeated often (i.e. opening and closing a door)

#You can write as pseudo code or use a flowchart before writing your final program. My Example is shown below:

#HERE IS AN EXAMPLE

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


