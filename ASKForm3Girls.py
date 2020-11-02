kekerapan = 0

flag = str(input("Adakah anda pernah ponteng sekolah? [Ya / Tidak]: "))

while ((flag.lower()) not in ["ya","tidak"]):
    flag = str(input("Adakah anda pernah ponteng sekolah? [Ya / Tidak]: "))
else:
    if flag.lower() == "ya":
        kekerapan = int(input("Masukkan bilangan hari anda telah ponteng: "))
        if kekerapan <= 1:
            print(" Anda akan dikenakan hukuman dengan dirotan sekali.") 
        elif kekerapan <= 3:
            print(" Anda akan dikenakan hukuman dengan dirotandua kali.") 
        elif kekerapan <= 5:
            print("Anda akan dikenakan hukuman dengan digantung sekolah selama seminggu.")
        else:
            print(" Anda akan dikenakan hukuman dengan dengan dibuang sekolah.")
    else:
        print("Anda seorang pelajar yang berdisiplin.")    
      
    
print("\nTerima kasih atas kerjasama anda")              