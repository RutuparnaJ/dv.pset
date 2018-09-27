#0091 Unique Random Numbers
import random 
arr=[]
i=0
num=0
for i in range(5):
    num=random.randrange(100000000000000000000)
    arr.append(num)
    for i in range(len(arr)-1):
        if arr[i]==num:
            arr.remove(num)
for i in range(5):
    print(arr[i])
    
