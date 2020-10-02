num = None
total = 0
turn = 0 
print("Masukkan nombor-nombor integer yang perlu dijumlahkan.")
print("Masukkan nombor 0 jika ingin berhenti memasukkan numbor.")

while num != 0:
    num = int(input())
    total += num
    turn += 1 

def average():
    return float(total / (turn - 1))
averageNum = average()    

print('\n' +"Jumlah nombor : "+ str(total))
print("Purata bagi nombor-nombor yang dimasukkan : "+ str(averageNum))