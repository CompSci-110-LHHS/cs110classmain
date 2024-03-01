### Python Classes, Class Methods, Class Variables ###

################ EXAMPLE 1 - Start ##################
############### UNCOMMENT BELOW TO RUN ##############  

# # This example defines a simple student class and prints some
# # attributes to the screen for two instances - student1 and student2

# class Student:

#     #Class Variable
#     schoolName = "Leo Hayes High School"
    
#     #Construct method, runs when a class instance is created
#     def __init__(self, first_name, last_name, age, grade):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.grade = grade
#         self.email = first_name + "." + last_name + "@school-email.com"

#     #setter and getter methods of editing instance attributes
#     def set_age(self, age): #setter function
#         self.age = age
    
#     def get_age(self): #getter function
#         return self.age

#     def set_grade(self, grade):
#         self.grade = grade
    
#     def get_grade(self):
#         return self.grade 

# #First Instance Created
# Student1 = Student("Hailey", "Powers", 17, 4)
# Student1.set_age(17)
# Student1.set_grade(4)

# #Second Instance Created
# Student2 = Student("Adam", "Day", 18, 3)
# Student2.set_age(17)
# Student2.set_grade(4)

# #Student1's Info
# print(Student1.get_age())
# print(Student1.get_grade())
# print(Student1.email)
# print(Student1.schoolName)

# #Student2's Info
# print(Student2.get_age())
# print(Student2.get_grade())
# print(Student2.email)
# print(Student2.schoolName)  
    
################ EXAMPLE 1 - END ##################



################ EXAMPLE 2 - Start ##################
############### UNCOMMENT BELOW TO RUN ##############  

class Student:
    #Class Variable
    schoolName = "Leo Hayes High School"
    totalSchoolDays = None    
    #Construct method, runs when a class instance is created
    def __init__(self, first_name, last_name, age=None, grade=None):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.grade = grade
        self.email = first_name + "." + last_name + "@school-email.com"
    #setter and getter methods of editing instance attributes
    def set_age(self, age): #setter function
        self.age = age    
    def get_age(self): #getter function
        return self.age
    def set_grade(self, grade):
        self.grade = grade    
    def get_grade(self):
        return self.grade 
        
    @staticmethod    #Static Method, doesn't depend class or instance variables
    def is_schoolDay(day):
        if day == "saturday" or day == "sunday":
            return "not a school day"
        else:
            return "go to class"
    
    @classmethod   #Class Method, takes the class as the first argument
    def set_schoolDays(cls, days):
        cls.totalSchoolDays = days
    

#First Instance Created
Student1 = Student("Hailey", "Powers")
print(Student1.get_age())
print(Student1.get_grade())
Student1.set_age(17)
Student1.set_grade(4)

#set Class Variable Using Class Method
Student.set_schoolDays(216)

#Student1's Info
print(Student1.get_age())
print(Student1.get_grade())
print(Student1.email)
print(Student1.schoolName)
print(Student.totalSchoolDays)
print(Student.is_schoolDay("thursday"))



        
################ EXAMPLE 1 - END ##################
    