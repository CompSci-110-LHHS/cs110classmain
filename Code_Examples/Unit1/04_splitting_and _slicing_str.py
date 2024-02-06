#Strings can me modified in useful ways. We can split them at a defined seperator (i.e. '-' below):
myString = "February-06-2024"
month, day, year = myString.split("-")

print(f"Month: {month}, Day: {day}, Year: {year}")

#CHALLENGE: Redo the above split using spaces instead of '-' between month, day and year

#Slices of a string and taken
onlyMonth = myString[0:8] #myString[:7] also works and means slice from beginning to the number defined (but not including that value)
print(onlyMonth)

#CHALLENGE: How would you slice only the year and store as a variable?

#Counting backwards
onlyDay = myString[-7:-5]
print(onlyDay)