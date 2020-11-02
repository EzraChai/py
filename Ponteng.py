kekerapan = 0

flag = str(input("Adakah anda pernah ponteng sekolah? [Ya / Tidak]: "))

while (flag.lower() not in ["ya","tidak"]):
    flag = str(input("Adakah anda pernah ponteng sekolah? [Ya / Tidak]: "))
else:
    if flag.lower() == "ya":
        kekerapan = int(input("Masukkan bilangan hari anda telah ponteng: "))
        if kekerapan <= 1:
            print("\nAnda akan dikenakan hukuman dengan dirotan sekali.") 
        elif kekerapan <= 3:
            print("\nAnda akan dikenakan hukuman dengan dirotan dua kali.") 
        elif kekerapan <= 5:
            print("\nAnda akan dikenakan hukuman dengan digantung sekolah selama seminggu.")
        else:
            print("\nAnda akan dikenakan hukuman dengan dengan dibuang sekolah.")
    else:
        print("\nAnda seorang pelajar yang berdisiplin.")    
      
    
print("\nTerima kasih atas kerjasama anda")              