################ Python Dictionary #################

# Dictionaries: ordered and changeable. Does Not Allow duplicate members.
# Dictionaries store data in key-values pairs. They are iterable and mutable (i.e. changable)

#Here are some examples:
studentInfo = {"first_name":"Jeff", "last_name":"McDowell", "Homeroom":"12H"}

#Longer Dictionaries can also be written with key-value pairs seperated on newlines:
studentInfo = {
    "first_name": "Jeff",
    "last_name":"McDowell",
    "Homeroom":"12H"
    }

#adding a new key-value pair can be done like your assigning a value to a key, even though the key does not yet exist
studentInfo["Roomnumber"] = "B216"

#new values can be assigned using the following syntax
studentInfo["first_name"] = "J"

#specific keys can be removed by name using pop()
studentInfo.pop("first_name")
print(studentInfo)

#Like lists, there are number of methods builtin to python to work with dictionaries. Some are:
    # clear()	Removes all the elements from the dictionary
    # copy()	Returns a copy of the dictionary    
    # get()	Returns the value of the specified key
    # items()	Returns a list containing a tuple for each key value pair
    # keys()	Returns a list containing the dictionary's keys
    # pop()	Removes the element with the specified key    
    # setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
    # update()	Updates the dictionary with the specified key-value pairs
    # values()	Returns a list of all the values in the dictionary

#Iterating through dicionaries, like lists, is down using a for loop:
cityWeather = {
    "City":"Fredericton",
    "Conditions":"Sunny",
    "Wind Speed": "8kn",
    "Temperature": -6,
    "Date": "2024-02-13"
    }

for conditions in cityWeather.items():  #Remember items() method returns the key-value pairs
    print("-------------")
    print(conditions)
    print("-------------")
    
#Nested Dictionaries are also possible - this starts to look like JSON formatted data returned from website API requests:
#List say we request weather data from NOAA, might get something that looks like this:

weatherInfo = {
    "Fredericton":{
        "Conditions":"Sunny",
        "Wind Speed": "8kn",
        "Temperature": -6,
        "Date": "2024-02-13"
        },
    "Moncton":{
        "Conditions":"Cloudy",
        "Wind Speed": "15kn",
        "Temperature": -7,
        "Date": "2024-02-13"
        }
    }

#If I want to know the current conditions in Monction, I need to nest down through the diction keys:
conditions = weatherInfo["Moncton"]["Conditions"]
print(conditions)  #OUTPUTS: Cloudy

#CHALLENGE: How would print the "Wind Speed" in Fredericton



















































# # List: ordered and changeable. Allows duplicate members.
# # Tuple: ordered and unchangeable. Allows duplicate members.
# # Set: unordered, unchangeable, and unindexed. No duplicate members.
# # Dictionary: ordered and changeable. Key-value pairs.


# ################   DICTIONARIES   #################

# #Addressing values/changing

# Get keys
# dict.keys()

# #Adding Items
# thisdict["color"] = "red"

# U#pdate Dictionary
# thisdict.update({"color": "red"})

# Removing Items
# pop()


# Del 
# del thisdict["model"]
# print(thisdict)


# Nest dictionaries

# clear()	Removes all the elements from the dictionary
# copy()	Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and value
# get()	Returns the value of the specified key
# items()	Returns a list containing a tuple for each key value pair
# keys()	Returns a list containing the dictionary's keys
# pop()	Removes the element with the specified key
# popitem()	Removes the last inserted key-value pair
# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	Updates the dictionary with the specified key-value pairs
# values()	Returns a list of all the values in the dictionary