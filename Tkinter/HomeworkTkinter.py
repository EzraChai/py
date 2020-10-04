from tkinter import *
from datetime import datetime,timedelta

root = Tk()
root.title("Masa")

e1 = None
e2 = None
output = None

tempohMasaTidur = None
waktuTidur = 0
waktuBangun = 0

def ChangeTime():
    Time1 = None
    Time2 = None
    Time1 = str(e1.get())
    Time2 = str(e2.get())
    
    waktuTidur = datetime.strptime(Time1, '%H:%M')
    waktuBangun = datetime.strptime(Time2, '%H:%M')

    if waktuTidur > waktuBangun :
        tempohMasaTidur = (waktuBangun + timedelta(1)) - waktuTidur
    elif waktuTidur < waktuBangun:
        tempohMasaTidur =  waktuBangun - waktuTidur
    elif waktuBangun == waktuTidur:
        tempohMasaTidur = timedelta(1)  

    minit = int(tempohMasaTidur.total_seconds()/60)

    jam = 0
    while minit >= 60:
        jam += 1 
        minit -= 60

    if jam == 0:
        x = ("Tidak memuaskan. Anda telah tidur: " + str(minit) + " minit")
    elif jam < 4:
        x =  ("Tidak memuaskan. ")
    elif jam < 6:
        x =  ("Memuaskan. ")
    elif jam < 8:
        x = ("Baik. ")
    else:
        x =  ("Cemerlang. ")
    output = str(x + "Anda telah tidur: " + str(jam)+" jam "+str(minit)+" minit")

    myLabel4 = Label(root,text="  ")
    myLabel4.grid(row=6)
    myLabel3 = Label(root,text=output)
    myLabel3.grid(row=7)
    myLabel5 = Label(root,text="  ")
    myLabel5.grid(row=8)
            

#Create a Label widget
myLabel1 = Label(root,text="Sila masukkan waktu TIDUR anda dalam format 24 jam [00:00]-[23:59]: ")
e1 = Entry(root,width="50",borderwidth="2")
myLabel2 = Label(root,text="Sila masukkan waktu BANGUN anda dalam format 24 jam [00:00]-[23:59]: ")
e2 = Entry(root,width="50",borderwidth="2")
myButton = Button(root,text="Hantar",command=ChangeTime)


#Pack it and show it
myLabel1.grid(row=0,column=0)
e1.grid(row=1,column=0)
myLabel2.grid(row=2,column=0)
e2.grid(row=3,column=0)
myButton.grid(row=5)


root.mainloop()