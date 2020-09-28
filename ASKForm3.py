from datetime import datetime,timedelta

#Masukkan waktu tidur dan bangun pengguna
Input_waktuTidur = str(input("Sila masukkan waktu TIDUR anda dalam format 24 jam [00:00]-[23:59]: ")) 
waktuTidur = datetime.strptime(Input_waktuTidur, '%H:%M')
Input_waktuBangun = str(input("Sila masukkan waktu BANGUN anda dalam format 24 jam [00:00]-[23:59]: "))
waktuBangun = datetime.strptime(Input_waktuBangun,'%H:%M')

#Cari tempoh waktu tidur
def CariTempohWaktuTidur():
    if waktuTidur > waktuBangun :
        return (waktuBangun + timedelta(1)) - waktuTidur
    elif waktuTidur < waktuBangun:
        return waktuBangun - waktuTidur
    else:
        return timedelta(1)

tempohMasaTidur = CariTempohWaktuTidur()

#Tukarkan masa kepada minit
def TukaranMasa(): 
    return int(tempohMasaTidur.total_seconds()/60)
    
minit = TukaranMasa()

#Tukarkan masa kepada jam dan minit
jam = 0
while minit >= 60:
    jam += 1 
    minit -= 60

#Output 
def output(minit,jam):
    Output = str(None)
    if jam < 4:
        Output = ("Tidak memuaskan.")
    elif jam < 6:
        Output = ("Memuaskan. ")
    elif jam < 8:
        Output = ("Baik. ")
    else:
        Output = ("Cemerlang. ")
    return(Output + "Anda telah tidur: " + str(jam)+" jam "+str(minit)+" minit")
         
print('\n'+output(minit,jam))           


