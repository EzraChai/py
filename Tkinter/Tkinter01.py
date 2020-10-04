from tkinter import *

root = Tk()

#Create a Label widget
myLabel = Label(root,text="Hello World")

#Pack it and show it
myLabel.grid(row=0,column=0)

root.mainloop()