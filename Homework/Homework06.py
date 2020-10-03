#ASK Form 2 PG 136
umur = int(input("Masukkan umur anda: "))
while umur < 0:
    umur = int(input("Masukkan umur anda: ")) 
if umur > 30:
    print("\nAnda ialah seorang dewasa.")
elif umur > 14:
    print("\nAnda ialah seorang belia.")
elif umur > 12:
    print("\nAnda ialah seorang remaja.")        
else:
    print("\nAnda ialah seorang kanak-kanak.")    