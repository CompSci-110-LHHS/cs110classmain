################ Python Tuples #################

# Tuples: ordered and unchangeable. Duplicate members are Allowed.
# Tuples can be iterated over but are not mutable (i.e. changable)

#Here are some examples:
yearlyPayRaise = (0.02, 0.05, 0.1, 0.1)

#You can print a value (or range) using indices like lists:
print(yearlyPayRaise[1])  #OUTPUTS: 0.05
print(yearlyPayRaise[1:])  #OUTPUTS: new tuple (0.05, 0.1, 0.1)

#Unpacking Tuples is a unique feature and stores its contents into individual variabls:
newEmp, seniorEmp, cfo, ceo = yearlyPayRaise
print(newEmp)
print(type(newEmp))  #You can see this now a float variable

#tuples can be extended with the '+' operator
moreEmpPays = (0.1, 0.2)
fullPayList = yearlyPayRaise + moreEmpPays
print(fullPayList)

#useful methods are identical to those for lists:
    # index()	Returns the index of the first element with the specified value
    # count()	Returns the number of elements with the specified value
