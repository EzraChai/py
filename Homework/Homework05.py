betul = 0
salah = 0
print("Jawab soalan-soalan berikut.")
print("a = 12 , b = 5, c = 2")
print("\n 1. a > b \n 2. a % b = 0 \n 3. 12 // 5 = c \n 4. a > 6 > b \n 5. b < 2 < a")

jaw1 = input("\nJawapan soalan 1: ")
jaw2 = input("Jawapan soalan 2: ")
jaw3 = input("Jawapan soalan 3: ")
jaw4 = input("Jawapan soalan 4: ")
jaw5 = input("Jawapan soalan 5: ")

if jaw1.lower() == "true":
    betul += 1
if jaw2.lower() == "false":
    betul += 1
if jaw3.lower() == "true":
    betul += 1 
if jaw4.lower() == "true":
    betul += 1   
if jaw5.lower() == "false":
    betul += 1

if betul == 5:
    print("\nTahniah, anda telah menjawab semua soalan dengan betul.")
else:
    salah = 5 - betul
    print("\nAnda telah menjawab "+ str(betul) +" soalan dengan betul dan " + str(salah) + " soalan dengan salah.")        




