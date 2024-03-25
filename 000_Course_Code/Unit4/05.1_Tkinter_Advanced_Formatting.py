from tkinter import *

root = Tk()
root.title("Advanced Formatting Cheatsheet")
root.minsize(width=400,height=300)


#Frames are used for basic groupings of elements
container = LabelFrame(root, padx=50, pady=50)
container.place(relx=0.5, rely=0.5, anchor="center")

upperFrame = Frame(container, width=200, height=50, bd=3, relief="sunken", bg="blue")
upperFrame.pack(pady=5)

middleFrame = Frame(container, width=200, height=50, bg="red")
middleFrame.pack(fill='both', pady=5)

bottomFrame = Frame(container, width=200, height=50, bg="green")
bottomFrame.pack(pady=5)

#Creating Labels, Entries and Buttons

button1 = Button(upperFrame, text="Button1").pack(side="left", padx=25, pady=25)
button2 = Button(upperFrame, text="Button2").pack(side="right", padx=25, pady=25)
button3 = Button(bottomFrame, text="Button3").place(relx=1,rely=1, anchor="se")
label1 = Label(middleFrame, text="This Is A Label", bg = "purple", fg="white").grid(row=0, column=0, sticky="e")
entry1 = Entry(middleFrame, width=25, bd=1, relief="sunken").grid(row=0, column=1, sticky="")


root.mainloop()