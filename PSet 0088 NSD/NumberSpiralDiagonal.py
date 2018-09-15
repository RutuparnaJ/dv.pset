#0088 Number Spiral Diagonal
i=0
j=0
c=0
n=2
Sum=1
edge=1001 #setting edge length
arr=range(1,edge*edge+1) #creating an array of natural numbers
for i in range (edge):
    for c in range(4):
        j=j+n #incrementing within on spiral arm (constant increment)
        print("j=",j, "arr[j]=",arr[j])
        Sum=Sum+arr[j]    #adding all numbers which fall on the diagonal    
    n=n+2 #incrementing n for one extra spiral arm
    print("Sum=",Sum)
    if(arr[j]==edge*edge):
        break
