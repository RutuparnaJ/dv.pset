#Bubble Sort
i=0
temp=0
arr = []

for i in range (11):
    element=int(input("Enter a number for the array: "))#reads a number one at a time
    arr.append(element)#appends the read number to the empty array created above
for i in range(11):
    print(arr[i]) #prints the complete array (checking whether program has collected data)
    
for j in range(11):       #for loop so that each number is checked with one another
    for i in range(10):
        if arr[i]>arr[i+1]:
            temp=arr[i]         #swapping the numbers if inequality is matched, hence sorting
            arr[i]=arr[i+1]
            arr[i+1]=temp

print("The sorted array is: ")
for i in range(11):
    print(arr[i])   #printing sorted array
