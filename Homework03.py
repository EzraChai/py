#FORM 2 ASK pg175
print("************* KUIZ MATEMATIK V1 *************")
skor = 0
nama = str(input("Masukkan nama anda: "))
print("Selamat datang ke Kuiz Matematik, < "+nama+" >")

def paparkanSkor(skor):
    return ("Skor anda: "+ str(skor))    

print("\nHitung hasil bagi 13 x 13.")
jawapan = int(input())
if jawapan == 169:
    skor += 5
    print("Tahniah")
    print(paparkanSkor(skor))
else:
    print("Maaf,jawapan ialah 169.")  
    print(paparkanSkor(skor))  

print("\nHitungkan hasil bagi 85 - ( 3 x 2 ).")
jawapan = int(input())
if jawapan == 79:
    skor += 5
    print("Tahniah")
    print(paparkanSkor(skor))
else:
    print("Maaf, jawapan ialah 79.")  
    print(paparkanSkor(skor))  

print("\nHitungkan hasil bagi ( 2 x 22 / 11 ) + 56 ")
jawapan = int(input())
if jawapan == 60:
    skor += 5
    print("Tahniah")
    print(paparkanSkor(skor))
else: 
    print("Maaf, jawapan ialah 78.") 
    print(paparkanSkor(skor))     

print("\n"+paparkanSkor(skor))

if skor == 15:
    print("Tahniah, Penguasaan Memuaskan.")
else:
    print("Usaha Lebih Gigih Lagi.")    

