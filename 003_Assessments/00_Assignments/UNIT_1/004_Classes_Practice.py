############################################################
################ UNIT 2: Python Classes ####################
################## Practice With Classes####################
############################################################

#Q: Write a python program Uses the ‘Student’ Class. Add another two Class attributes: Hobby and Favorite Programming Language and print that to the screen for a student instance of that class: 

#Hint Consider the Example Code:



class Student:
    #Class constructor, a special function that always runs
    #When a new class instance is made
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.email = first_name + "." + last_name + "@school-email.com"

    #Instance Variable
    age = None
    def set_age(self, age): #setter function
        self.age = age
    
    def get_age(self): #getter function
        return self.age

    grade = None
    def set_grade(self, grade):
        self.grade = grade
    
    def get_grade(self):
        return self.grade
    
    def get_email(self):
        return self.email    

Student1 = Student("Hailey", "Powers")
Student1.set_age(17)
Student1.set_grade(4)

print(Student1.get_age())
print(Student1.get_grade())
print(Student1.get_email())
print(Student1.email)
print(Student1.first_name)