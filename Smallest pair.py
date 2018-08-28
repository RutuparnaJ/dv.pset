# smallest pair
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

print("The smallest pair is: ", arr[0], arr[1])
