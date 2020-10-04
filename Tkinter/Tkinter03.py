#Create a button

from tkinter import *
root = Tk()

def myClick():
    myLabel = Label(root,text="HelloWorld")
    myLabel.pack()
myButton = Button(root,text="Click me!",padx=50,pady=50,command=myClick,fg="blue",bg="orange")

myButton.pack()

root.mainloop()