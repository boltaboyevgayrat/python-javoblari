arr = []
while True:
    a = int(input("Massiv elementini kiriting:  "))
    arr.append(a)
    xabar = input("Yana element qo'shasizmi? (ha/yo'q)")
    if xabar != "ha":
        break

print(arr)    

max_in = None
min_in = None
index =  0
while True:
    if arr[index] == max(arr):
        max_in = index
    if arr[index] == min(arr):
        min_in = index
        
    index += 1
    if (max_in != None and min_in != None):
        break

arr[max_in], arr[min_in] = min(arr), max(arr)
 

print(arr)