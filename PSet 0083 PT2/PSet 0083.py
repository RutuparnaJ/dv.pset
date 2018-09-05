#0083 Pythagorean Triplet 2
arr=[]
i=0
print("Enter 3 numbers to check whether they are a Pythagorean Triplet or not")
for i in range(3):
    element=int(input())  #inputs 3 numbers in the form of a array
    arr.append(element)
arr.sort()                #sorts the array
a=arr[0]
b=arr[1]
c=arr[2]                 # assigns the largest side value to c

if a*a + b*b == c*c:     #checks the pythagorean formula
    print("true")
    print("provided c=",c)
else:
    print("false")
