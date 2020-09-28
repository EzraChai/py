from datetime import datetime,timedelta

jam = 0
Input_waktuTidur = str(input("Sila masukkan waktu TIDUR anda dalam format 24 jam [00:00]-[23:59]: ")) 
waktuTidur = datetime.strptime(Input_waktuTidur, '%H:%M')
Input_waktuBangun = str(input("Sila masukkan waktu BANGUN anda dalam format 24 jam [00:00]-[23:59]: "))
waktuBangun = datetime.strptime(Input_waktuBangun,'%H:%M')

if waktuTidur > waktuBangun :
    tempohMasaTidur = (waktuBangun + timedelta(1)) - waktuTidur
else:
    tempohMasaTidur = waktuBangun - waktuTidur

tempoh = float(tempohMasaTidur.total_seconds())
tempoh /= 60
minit = int(tempoh)    

while minit >= 60:
    jam += 1 
    minit -= 60
 
def output(minit,jam):
    if jam < 4:
        return("Tidak memuaskan. Anda hanya tidur: " + str(jam)+" jam "+str(minit)+" minit")
    elif jam < 6:
        return("Memuaskan. Anda telah tidur: " + str(jam)+" jam "+str(minit)+"minit")
    elif jam < 8:
        return("Baik. Anda telah tidur: " + str(jam)+" jam "+str(minit)+" minit")
    else:
        return("Cemerlang. Anda telah tidur: " + str(jam)+" jam "+str(minit)+" minit")         

print()
print(output(minit,jam))           


