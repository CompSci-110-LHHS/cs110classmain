################ Python tkinter module for graphical interfaces #################

#THese examples higlight more advanced tkinter functions
#and show how access values stored in text entry fields and
#checkbuttons and store them in variables

################ EXAMPLE 1 - Start ##################
############### UNCOMMENT BELOW TO RUN ##############

from tkinter import *

#Function
def submit():
    print("Record Created!")

root = Tk()
root.title("Student Record Form")

#Frames are how we group widgets
mainFrame = Frame(root, padx=10,pady=10)
mainFrame.pack()
upperFrame = Frame(mainFrame, pady=10)
upperFrame.pack()
middleFrame = Frame(mainFrame)
middleFrame.pack()
bottomFrame = Frame(mainFrame, pady=10)
bottomFrame.pack()

#Labels are a simple widget example
topTitle = Label(upperFrame, text="Student Record Creation Form")
topTitle.pack()

studentID = Label(middleFrame, text="Student ID", padx=5)
studentID.grid(row=0, column=0, sticky=E)
idField = Entry(middleFrame,)
idField.grid(row=0,column=1)

first_name = Label(middleFrame, text="First Name", padx=5)
first_name.grid(row=1, column=0, sticky=E)
fnameField = Entry(middleFrame)
fnameField.grid(row=1,column=1)

last_name = Label(middleFrame, text="Last Name", padx=5)
last_name.grid(row=2, column=0, sticky=E)
lnameField = Entry(middleFrame)
lnameField.grid(row=2,column=1)

age = Label(middleFrame, text="Age", padx=5)
age.grid(row=3, column=0, sticky=E)
ageField = Entry(middleFrame)
ageField.grid(row=3,column=1)

gradeLevel = Label(middleFrame, text="Grade Level", padx=5)
gradeLevel.grid(row=4, column=0, sticky=E)
gradeField = Entry(middleFrame)
gradeField.grid(row=4,column=1)

gpa = Label(middleFrame, text="Current GPA", padx=5)
gpa.grid(row=5, column=0, sticky=E)
gpaField = Entry(middleFrame)
gpaField.grid(row=5,column=1)

submitButton = Button(bottomFrame, text="Submit", command=submit,)
submitButton.pack()

root.mainloop()


################ EXAMPLE 1 - Start ##################