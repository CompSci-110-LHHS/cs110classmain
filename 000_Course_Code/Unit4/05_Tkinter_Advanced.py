################ Python tkinter module for graphical interfaces #################

#THese examples higlight more advanced tkinter functions
#and show how access values stored in text entry fields and
#checkbuttons and store them in variables

################ EXAMPLE 1 - Start ##################
############### UNCOMMENT BELOW TO RUN ##############

from tkinter import *
import csv
from PIL import ImageTk, Image

#Function
def submit():
    with open("student_database.csv", "a", newline="") as db:
        fieldnames = ["ID", "First Name", "Last Name", "Age", "Grade Level", "GPA", "Grad?"]
        dbwriter = csv.DictWriter(db, fieldnames=fieldnames)        
        dbwriter.writerow({"ID": idField.get(), "First Name":fnameField.get(), "Last Name":lnameField.get(), "Age":ageField.get(), "Grade Level":gradeField.get(), "GPA":gpaField.get(), "Grad?":isGrad.get()})    

    print(f"Record Created! For {fnameField.get()} {lnameField.get()}")
    statusMsg.set("New Record Created") 
    #Clear The Form
    idField.delete(0,END)
    fnameField.delete(0,END)
    lnameField.delete(0,END)
    ageField.delete(0,END)
    gradeField.delete(0,END)
    gpaField.delete(0,END)

root = Tk()
root.title("Student Record Form")
root.minsize(width=400,height=400)
root.iconbitmap("lhhs_logo.ico")



#Variables
statusMsg = StringVar()
statusMsg.set("Ready...")
isGrad = BooleanVar()
isGrad.set(False)

lhhs_logo = ImageTk.PhotoImage(Image.open("LHHS_Logo_Full.png"))


#Frames are how we group widgets
mainFrame = LabelFrame(root, padx=10, pady=10)
mainFrame.place(relx=0.5, rely=0.5, anchor="center")
upperFrame = Frame(mainFrame, pady=10)
upperFrame.pack()
middleFrame = Frame(mainFrame)
middleFrame.pack()
bottomFrame = Frame(mainFrame, pady=10)
bottomFrame.pack()
statusFrame = Frame(root)
statusFrame.pack(side="bottom", fill=X, anchor="w")

#Labels are a simple widget example

topLogo = Label(upperFrame, image=lhhs_logo)
topLogo.pack()
topTitle = Label(upperFrame, text="Student Record Creation Form")
topTitle.pack()

studentID = Label(middleFrame, text="Student ID", pady=2)
studentID.grid(row=0, column=0, sticky=E)
idField = Entry(middleFrame)
idField.grid(row=0,column=1)

first_name = Label(middleFrame, text="First Name", pady=2)
first_name.grid(row=1, column=0, sticky=E)
fnameField = Entry(middleFrame)
fnameField.grid(row=1,column=1)

last_name = Label(middleFrame, text="Last Name", pady=2)
last_name.grid(row=2, column=0, sticky=E)
lnameField = Entry(middleFrame)
lnameField.grid(row=2,column=1)

age = Label(middleFrame, text="Age", pady=2)
age.grid(row=3, column=0, sticky=E)
ageField = Entry(middleFrame)
ageField.grid(row=3,column=1)

gradeLevel = Label(middleFrame, text="Grade Level", pady=2)
gradeLevel.grid(row=4, column=0, sticky=E)
gradeField = Entry(middleFrame)
gradeField.grid(row=4,column=1)

gpa = Label(middleFrame, text="Current GPA", pady=2)
gpa.grid(row=5, column=0, sticky=E)
gpaField = Entry(middleFrame)
gpaField.grid(row=5,column=1)

gradCheck = Checkbutton(middleFrame, text="Graduating?", variable=isGrad)
gradCheck.grid(row=6,columnspan=2)

submitButton = Button(bottomFrame, text="Submit", width=50, command=submit)
submitButton.pack()

status = Label(statusFrame, textvariable=statusMsg, bd=1, relief="ridge", anchor="w").pack(side="bottom",fill=X)

root.mainloop()


################ EXAMPLE 1 - Start ##################