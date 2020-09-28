from datetime import datetime,timedelta

#Masukkan waktu tidur dan bangun pengguna
Input_waktuTidur = str(input("Sila masukkan waktu TIDUR anda dalam format 24 jam [00:00]-[23:59]: ")) 
waktuTidur = datetime.strptime(Input_waktuTidur, '%H:%M')
Input_waktuBangun = str(input("Sila masukkan waktu BANGUN anda dalam format 24 jam [00:00]-[23:59]: "))
waktuBangun = datetime.strptime(Input_waktuBangun,'%H:%M')

#Cari tempoh waktu tidur
if waktuTidur > waktuBangun :
    tempohMasaTidur = (waktuBangun + timedelta(1)) - waktuTidur
elif waktuTidur < waktuBangun:
    tempohMasaTidur = waktuBangun - waktuTidur
else:
    tempohMasaTidur = timedelta(1)

#Tukarkan masa kepada minit
tempoh = float(tempohMasaTidur.total_seconds())
minit = int(tempoh / 60)    

#Tukarkan masa kepada jam dan minit
while minit >= 60:
    jam += 1 
    minit -= 60

#Output 
def output(minit,jam):
    if jam < 4:
        return("Tidak memuaskan. Anda hanya tidur: " + str(jam)+" jam "+str(minit)+" minit")
    elif jam < 6:
        return("Memuaskan. Anda telah tidur: " + str(jam)+" jam "+str(minit)+" minit")
    elif jam < 8:
        return("Baik. Anda telah tidur: " + str(jam)+" jam "+str(minit)+" minit")
    else:
        return("Cemerlang. Anda telah tidur: " + str(jam)+" jam "+str(minit)+" minit")         

print()
print(output(minit,jam))           


