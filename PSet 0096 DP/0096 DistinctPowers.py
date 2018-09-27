#0096 Distinct Powers
import math #imports math function so we can use the power function
a=2
b=2
i=0
element=0
arr=[]
for a in range(2,101):
    for b in range (2,101):
        element=math.pow(a,b) #finds a raised to b
        arr.append(element) #appends the element to the array to count numbers
        #print(len(arr))
        for i in range (len(arr)-1):
            if element==arr[i]:  #checking repetition
                arr.remove(int(element)) #if found, element is deleted from the array
            
print("Length of array: ",len(arr)+1)
#for i in range(len(arr)):
    #print(arr[i])
