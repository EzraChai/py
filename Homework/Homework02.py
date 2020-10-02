#FORM 2 ASK pg149
print("***ATUR CARA INI AKAN MENJANA JADUAL SIFIR DARAB ***")
num = int(input("Masukkan nombor Jadual Sifir Darab anda: "))
print("Jadual sifir Darab " + str(num) + " ialah: ")
for i in range(1,13):
    print(str(i) +" x " + str(num) + " = " + str(i*num))
