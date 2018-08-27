#Repeated numbers
arr = []
for i in range (11):
    element=int(input("Enter a number for the array: "))
    arr.append(element)
for i in range(11):
    print(arr[i])
arr.sort()
print("The sorted array is: ")
for i in range(11):
    print(arr[i])
print("The repeated numbers are: ")
for i in range(12):
    if(arr[i]==arr[i+1]):
        print(arr[i])
