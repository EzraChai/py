#FORM 2 ASK pg175
#FIX BUG
nama = str(input("Masukkan nama anda: "))
while nama == "":
   nama = str(input ("Sila masukkan nama anda: "))
else:
    umur = int(input("Masukkan umur anda: "))
    while umur <= 0:
     print ("Umur anda mesti lebih daripada 0.")
     umur = int(input ("Masukkan umur anda: "))
    else:
     print ("Salam sejahtera "+ nama + ". Anda berumur "+
str(umur)+ " tahun.")