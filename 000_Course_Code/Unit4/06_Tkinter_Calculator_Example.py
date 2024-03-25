from tkinter import *

root = Tk()
root.title("Calculator App")
root.minsize(width=400, height=300)
# root.iconbitmap("lhhs_logo.ico")
#taskbar Icon
small_icon = PhotoImage(file="LHHS_Logo_16x16.png")
large_icon = PhotoImage(file="LHHS_Logo_64x64.png")
root.iconphoto(False,large_icon, small_icon)

#Global Variables
inputString = StringVar()
inputString.set("")

#Methods
def expression(value):
    current = inputString.get()
    new = current + value
    inputString.set(new)

def eval():
    pass

#Frames
main = LabelFrame(root, padx=5, pady=5)
main.place(relx=0.5, rely=0.5, anchor="center")

buttonFrame = Frame(main)
buttonFrame.pack()

#Elements
inputField = Label(buttonFrame, textvariable=inputString,bd=2, relief="sunken", bg="white", height=4)
inputField.grid(row=0, columnspan=4, sticky="nwse",pady=5)

#First Num Button Row
button7 = Button(buttonFrame, text = "7", width=5, height=2, command=lambda: expression("7"))
button7.grid(row=1, column=0)
button8 = Button(buttonFrame, text = "8", width=5, height=2, command=lambda: expression("8"))
button8.grid(row=1, column=1)
button9 = Button(buttonFrame, text = "9", width=5, height=2, command=lambda: expression("9"))
button9.grid(row=1, column=2)
buttonDiv = Button(buttonFrame, text = "/", width=5, height=2, command=lambda: expression(" / "))
buttonDiv.grid(row=1, column=3)
#Second Num Button Row
button4 = Button(buttonFrame, text = "4", width=5, height=2, command=lambda: expression("4"))
button4.grid(row=2, column=0)
button5 = Button(buttonFrame, text = "5", width=5, height=2, command=lambda: expression("5"))
button5.grid(row=2, column=1)
button6 = Button(buttonFrame, text = "6", width=5, height=2, command=lambda: expression("6"))
button6.grid(row=2, column=2)
buttonMult = Button(buttonFrame, text = "X", width=5, height=2, command=lambda: expression(" x "))
buttonMult.grid(row=2, column=3)
#Third Num Button Row
button1 = Button(buttonFrame, text = "1", width=5, height=2, command=lambda: expression("1"))
button1.grid(row=3, column=0)
button2 = Button(buttonFrame, text = "2", width=5, height=2, command=lambda: expression("2"))
button2.grid(row=3, column=1)
button3 = Button(buttonFrame, text = "3", width=5, height=2, command=lambda: expression("3"))
button3.grid(row=3, column=2)
buttonMin = Button(buttonFrame, text = "-", width=5, height=2, command=lambda: expression(" - "))
buttonMin.grid(row=3, column=3)
#Forth Num Button Row
buttonSign = Button(buttonFrame, text = "+/-", width=5, height=2)
buttonSign.grid(row=4, column=0)
button0 = Button(buttonFrame, text = "0", width=5, height=2, command=lambda: expression("0"))
button0.grid(row=4, column=1)
buttonDot = Button(buttonFrame, text = ".", width=5, height=2, command=lambda: expression("."))
buttonDot.grid(row=4, column=2)
buttonPls = Button(buttonFrame, text = "+", width=5, height=2, command=lambda: expression(" + "))
buttonPls.grid(row=4, column=3)

#Calculate And Clear Buttons
calculate = Button(buttonFrame, text="Enter")
calculate.grid(row=5, columnspan=2, column=0, sticky="nwse")
clear = Button(buttonFrame, text="Clear", command=lambda: inputString.set(""))
clear.grid(row=5, columnspan=2, column= 2, sticky="nwse")


root.mainloop()

