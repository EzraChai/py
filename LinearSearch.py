list = [10,82,5,18,27,15,44,100,42,99]
i = 0
n = 10
target = 27

while i < n:
    if list[i] == target:
        print("Item ["+ str(target) +"] founded in the list in index of ["+ str(i) +"]")
        break
    else:
        i += 1
if i >= n:
    print("Item ["+ str(target) +"] is not found ")       
