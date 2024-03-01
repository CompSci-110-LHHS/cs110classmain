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