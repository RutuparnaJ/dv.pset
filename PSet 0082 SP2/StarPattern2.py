# 0082 Star Pattern 2
i=0
j=0
n=int(input("enter a number: "))
for i in range(n):
     while(j<i):     #checking whether the columnns are less than rows
        print("*", end="")
        j=j+1        # incrementing column value
     if(j==i):
         j=0           #resetting column value to zero
         print()
for i in range(n):
    while(j<n):     #checking whether the columnns are less than rows
        print("*", end="")
        j=j+1        # incrementing column value
    if(j==n):         
        n=n-1       #decrementing the value of n so that the number of columns are always one less than the ith row
        j=0           #resetting column value to zero
        print()
