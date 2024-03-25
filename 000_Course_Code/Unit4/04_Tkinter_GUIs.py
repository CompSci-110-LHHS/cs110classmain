################ Python tkinter module for graphical interfaces #################

#Python has a module called 'tkinter' for working with graphics
# Basic tkinter programs contain a main window (often named 'root') which can 
# divided into frames. Elements including buttons, text boxes, labels, graphs
# images etc...collectively called widgets can be organized with frames to 
# resemble a modern looking program we are all familiar with. Let's start
# with some simple examples 

################ EXAMPLE 1 - Start ##################
############### UNCOMMENT BELOW TO RUN ##############
# from tkinter import *

# root = Tk() #creates an instance of the Tk() class - basically the 'main' window

# #Frames are how we group widgets
# upperFrame = Frame(root)
# upperFrame.pack(side="top")

# bottomFrame = Frame(root)
# bottomFrame.pack(side='bottom')

# #Labels are a simple widget that are just text labels
# topLabel1 = Label(upperFrame, text="Hello CS110, here is a Tkinter Example With Buttons")
# topLabel1.pack()

# #Button are another simple widget that trigger an action (a method)
# lButton = Button(bottomFrame, text="Left Button")
# lButton.pack(side="left", pady=10, padx=5)
# mButton = Button(bottomFrame, text="Middle Button")
# mButton.pack(side="left", pady=10, padx=5)
# rButton = Button(bottomFrame, text="Right Button")
# rButton.pack(side="left", pady=10, padx=5)
# check = Checkbutton(bottomFrame, text="Check Button")
# check.pack(side="left", pady=10, padx=5)

# root.mainloop() #The mainloop() method creates an endless loop that keeps the window open

################ EXAMPLE 1 - End ##################


################ EXAMPLE 2 - Start ##################
############### UNCOMMENT BELOW TO RUN ##############
# from tkinter import *

# def loginMessage():
#     print("Login Success!")
#    

# root = Tk()
# #Frames are how we group widgets
# upperFrame = Frame(root)
# upperFrame.pack()
# middleFrame = Frame(root)
# middleFrame.pack()
# bottomFrame = Frame(root)
# bottomFrame.pack()

# #Labels are a simple widget example
# topTitle = Label(upperFrame, text="Welcome User, Please Login")
# topTitle.pack()

# name = Label(middleFrame, text="Username/Email", padx=5)
# name.grid(row=0, column=0,  sticky="E")
# nameField = Entry(middleFrame)
# nameField.grid(row=0,column=1)

# password = Label(middleFrame, text="Password", padx=5)
# password.grid(row=1, column=0, sticky="E")
# passwordField = Entry(middleFrame)
# passwordField.grid(row=1,column=1)

# submitButton = Button(bottomFrame, text="Submit", command=loginMessage)
# submitButton.pack()

# root.mainloop()
################ EXAMPLE 2 - End ##################


################ EXAMPLE 3 - Start ##################
############### UNCOMMENT BELOW TO RUN ##############
from tkinter import *

root = Tk()
root.title("Login Window")

#Function
def printMessage():
    print("Login Successful!")

#Frames are how we group widgets
upperFrame = Frame(root)
upperFrame.pack()
middleFrame = Frame(root)
middleFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack()

#Labels are a simple widget example
topTitle = Label(upperFrame, text="Welcome User, Please Login", fg="blue")
topTitle.pack()

name = Label(middleFrame, text="Username/Email")
name.grid(row=0, column=0, sticky=E)
nameField = Entry(middleFrame)
nameField.grid(row=0,column=1)

password = Label(middleFrame, text="Password")
password.grid(row=1, column=0, sticky=E)
passwordField = Entry(middleFrame)
passwordField.grid(row=1,column=1)

submitButton = Button(bottomFrame, text="Submit", command=printMessage)
submitButton.pack()

root.mainloop()
################ EXAMPLE 3 - End ##################

