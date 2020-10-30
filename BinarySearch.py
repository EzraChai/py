list = [13,213,213,434,554,2,42,113,143,44,4,24654,76,546,3,275,5,25,552,5,5,45,352,45,2,65,544]
list.sort()

n = len(list)
i = 0
j = n - 1
b = 546

print(list)

while i <= j:
    print("loop")
    m = int((i + j)/2)
    print("number = ",list[m])
    if b == list[m]:
        print("Item["+str(b)+"] founded in index of ["+str(m)+"]") 
        break
    else:
        if b < list[m]:
            print(list[m], "less than ,index ", m)
            j = m - 1
            print("j",j)
        else:
            print(list[m], "more than ,index ", m)
            i = m + 1
            print("i",i)

if i > j:
    print("Item not found")