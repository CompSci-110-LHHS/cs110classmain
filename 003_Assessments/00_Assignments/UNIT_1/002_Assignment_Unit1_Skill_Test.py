#String Formatting

###########################  Question 1 ###########################   
# Write a program that takes your first, middle and last name as a single string and reformats it to "lastname, first middle initial"
#ex. Jeffrey Jared McDowell --> McDowell, Jeffrey J

###########################  Question 2 ########################### 
#(PART 1) Take the string below and split the values on the comma and store the first name, last_name, age, grade
# in a dictionary of dictionaries (HINT: use the student_ID as the key for the outermost dictionary)

#This string stores: first_name, last_name, age, grade, student_ID
student1 = "Adam,Day, 18, 4, 1001224"
student2 = "Cassie, Stevens, 16, 1, 1005644"
student3 = "Hailey, Powers, 17, 4, 120534"

studentDatabase = {
    "1001224":{
        "first_name":"Adam",
        "last_name": "Day",
        "Age": 18,
        "Grade": 4
        }
    }

print(studentDatabase["1001224"]["last_name"])

print("Please input student ID: ", end="")
searchKey = input()

print(studentDatabase[____BLANK_____]["last_name"])









# studentDatabase = {}

# students = [student1, student2, student3]

# for student in students:
#     fname, lname, age, grade, sID = student.split(",")
#     # print(fname)
#     # print(lname)
#     # print(age)
#     # print(grade)
#     # print(sID)

#     studentRecord = {
#         "first_name":fname.strip(),
#         "last_name":lname.strip(),
#         "Age": age.strip(),
#         "Grade":grade.strip(),
#         }
#     print(studentRecord)

#     sID = sID.split()

#     studentDatabase = {sID:studentRecord}


# print(studentDatabase)


# student1 = "Adam,Day, 18, 4, 1001224"
# student2 = "Cassie, Stevens, 16, 1, 1005644"
# student3 = "Hailey, Powers, 17, 4, 120534"

#(PART 2)Write a program that will take a user search input for student_ID and print that students info to the screen

###########################  Question 3 ########################### 
#Take the above example and add another key value in each students dictionary that evaluates to 'Great' or 'Good' and 'Needs Improvment' for grades >3, 2 <= grade <= 3, and < 1 


###########################  Question 4 ########################### 
#Draw the following shapes using nested 'for loops'

#       * * * * * * * * 
#       * * * * * * * *
#       * * * * * * * *
#       * * * * * * * *
#       * * * * * * * *
#       * * * * * * * *
#       * * * * * * * *
#       * * * * * * * *  

#       * * * * * * * *
#       *             *
#       *             *
#       *             *
#       *             *
#       *             *
#       *             *
#       * * * * * * * *

#       * * * * * * * *
#       * * * * * * *
#       * * * * * *
#       * * * * *
#       * * * *
#       * * *
#       * *
#       *

#       * * * * * * * *
#       *           *
#       *         *
#       *       *
#       *     *
#       *   *
#       * *
#       *


#edit the program so it takes a user input for the shape size
#HINT: use input = int(input) to get and int variable
