amaun = 0.0
jumlah = 0.0

RM20 = 0
RM10 = 0
RM1 = 0
Sen20 = 0
Sen10 = 0

def printStar():
    print("*******************************************************************************")

def Pulangkan(Baki,RM20,RM10,RM1,Sen20,Sen10):
    while (Baki >= 20.0):
        RM20 += 1
        Baki -= 20.0
        Baki = round(Baki,2)
    while (Baki >= 10.0):
        RM10 += 1
        Baki -= 10.0
        Baki = round(Baki,2)
    while (Baki >= 1.0):    
        RM1 += 1
        Baki -= 1.0
        Baki = round(Baki,2)
    while (Baki >= 0.2):
        Sen20 += 1
        Baki -= 0.2
        Baki = round(Baki,2)
    while (Baki >= 0.1):
        Sen10 += 1
        Baki -= 0.1
        Baki = round(Baki,2)    

    return RM20,RM10,RM1,Sen20,Sen10

def MasukkanAmaun(amaun,jumlah):
    while(amaun != "T"):
        print("Teruskan atau Masukkan T untuk mendapatkan JUMLAH:")
        amaun = str(input("Masukkan amaun: "))
        if amaun.lower() == "t":
            break
        else:
            jumlah += float(amaun)
    return jumlah  

def cariBaki():
    return float(amaunDiterima-float(jumlah))

print("                KEDAI RUNCIT PAKCIK SAIRIN                ")
jumlah = MasukkanAmaun(amaun,jumlah)

print("\nJumlah belian: RM",jumlah)
amaunDiterima = int(input("Masukkan amaun diterima: RM "))
printStar()
print("Terima (RM): " + str(amaunDiterima))
print("Jumlah belian (RM): " + str(jumlah))
Baki = cariBaki()
print("Baki (RM): " +str(round(Baki,2)))
print("\nPulangkan.....")
printStar()
[RM20,RM10,RM1,Sen20,Sen10] = Pulangkan(Baki,RM20,RM10,RM1,Sen20,Sen10)
print("RM20: "+ str(RM20))
print("RM10: "+ str(RM10))
print("RM1: "+ str(RM1))
print("20sen: "+ str(Sen20))
print("10sen: "+ str(Sen10))
printStar()


