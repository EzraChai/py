from datetime import datetime,timedelta

waktuTidur = 0
waktuBangun = 0
jam = 0
minit = 0

#Pengguna memasukkan Waktu Tidur dan Waktu Bangun
def InputPengguna():
    input_waktuTidur = str(input("Sila masukkan waktu TIDUR anda dalam format 24 jam [00:00]-[23:59]: ")) 
    waktuTidur = datetime.strptime(input_waktuTidur, '%H:%M')
    input_waktuBangun = str(input("Sila masukkan waktu BANGUN anda dalam format 24 jam [00:00]-[23:59]: "))
    waktuBangun = datetime.strptime(input_waktuBangun,'%H:%M')
    return waktuTidur,waktuBangun

#Cari Tempoh Masa Tidur
def CariTempohMasaTidur(waktuTidur,waktuBangun):
    if waktuTidur > waktuBangun :
        return (waktuBangun + timedelta(1)) - waktuTidur
    elif waktuTidur < waktuBangun:
        return waktuBangun - waktuTidur
    else:
        return timedelta(0)

#Tukar Tempoh Masa Tidur kepada Jam dan Minit
def TukaranTempohMasaTidur(jam,minit): 
    minit = int(tempohMasaTidur.total_seconds()/60)
    while minit >= 60:
        jam += 1 
        minit -= 60
    return minit , jam    

#Output 
def output(minit,jam):
    if jam == 0:
        print("\nTidak memuaskan. Anda telah tidur: " + str(minit) + " minit")
        return
    elif jam < 4:
        Output = ("Tidak memuaskan. ")
    elif jam < 6:
        Output = ("Memuaskan. ")
    elif jam < 8:
        Output = ("Baik. ")
    else:
        Output = ("Cemerlang. ")
    print("\n" + Output + "Anda telah tidur: " + str(jam) + " jam " + str(minit) + " minit")
    return

#Main
[waktuTidur,waktuBangun] = InputPengguna()
tempohMasaTidur = CariTempohMasaTidur(waktuTidur,waktuBangun)     
[jam,minit] = TukaranTempohMasaTidur(jam,minit)    
output(jam,minit)