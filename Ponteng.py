kekerapan = 0

# Pengguna memasukkan Ya atau Tidak pernah ponteng
# Jika pengguna memasukki Input yang salah, system akan mengulangi sekali lagi
def Ponteng():
    flag = str(input("Adakah anda pernah ponteng sekolah? [Ya / Tidak]: "))

    while (flag.lower() not in ["ya","tidak"]):
        print("Sila hanya memasuki [Ya atau Tidak].")
        flag = str(input("Adakah anda pernah ponteng sekolah? [Ya / Tidak]: "))
    return flag

# Proses dan Output
def Proses(flag):
    if flag.lower() == "ya":
        kekerapan = int(input("Masukkan bilangan hari anda telah ponteng: "))
        while kekerapan < 0:
            print("Tolong masukkan bilangan hari yang betul.")
            kekerapan = int(input("Masukkan bilangan hari anda telah ponteng: "))
        if kekerapan <= 1:
            return("\nAnda akan dikenakan hukuman dengan dirotan sekali.") 
        elif kekerapan <= 3:
            return("\nAnda akan dikenakan hukuman dengan dirotan dua kali.") 
        elif kekerapan <= 5:
            return("\nAnda akan dikenakan hukuman dengan digantung sekolah selama seminggu.")
        else:
            return("\nAnda akan dikenakan hukuman dengan dengan dibuang sekolah.")
    else:
        return("\nAnda seorang pelajar yang berdisiplin.")    
      
# Main
flag = Ponteng()
print(Proses(flag))      
print("\nTerima kasih atas kerjasama anda")              
