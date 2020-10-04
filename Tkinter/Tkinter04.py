#Create Entry aka Input

from tkinter import *
root = Tk()

def myClick():
    myLabel = Label(root,text="Welcome, "+e.get())
    myLabel.pack()

myLabel1 = Label(root,text="Please enter your name.")
myLabel1.pack()

e = Entry(root,width="50",borderwidth="2")
e.pack()
e.insert(0,"Name :  ")

myButton = Button(root,text="Submit",command=myClick)

myButton.pack()

root.mainloop()