############# Python Classe Inheritance ##############

################ EXAMPLE 1 - Start ##################
############### UNCOMMENT BELOW TO RUN ##############  

class Student:
    #Instance Variable
    schoolName = "Leo Hayes High School"
    numSchoolDays = 216

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.email = first_name + "." + last_name + "@school-email.com"   

    def full_name(self):
        return self.first_name + " " + self.last_name

    @staticmethod    #Static Method, doesn't depend class or instance variables
    def is_schoolDay(day):
        if day == "saturday" or day == "sunday":
            return "not a school day"
        else:
            return "go to class"
    
    @classmethod   #Class Method, takes the class as the first argument
    def set_schoolDays(cls, days):
        cls.numSchoolDays = days 

class Teacher(Student):
    numSchoolDays = 230
    raise_amount = 1.05

    def __init__(self, first_name, last_name, subject, pay):
        super().__init__(first_name, last_name)
        self.subject = subject
        self.pay = pay

    
    def apply_raise(self):
        self.pay = self.pay * self.raise_amount        
    
    @classmethod
    def set_raise(cls, raise_amount):
        cls.raise_amount = raise_amount

Student1 = Student("Adam", "Day")
Teacher1 = Teacher("Jeff", "McDowell", "Computer Science", 65000)

print(Student1.full_name())
print(Teacher1.full_name())
print(Teacher1.email)
print(f"Original Pay Is: {'%.2f' % Teacher1.pay}")
Teacher1.apply_raise()
print(f"New Pay Is: {'%.2f' % Teacher1.pay}")








      
     
    
################ EXAMPLE 1 - Start ##################