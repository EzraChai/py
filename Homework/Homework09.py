pi = 3.142
jejari = float(input("Masukkan jejari: "))

def kiraIsiPaduSfera():
    return 4 / 3 * pi * pow(jejari,3)

print("Isi padu sfera yang berjejari ",jejari ," ialah ",round(kiraIsiPaduSfera(),4)," sentimeter padu")