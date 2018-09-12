#0062 Lattice Paths
i=1
fact=1
n=int(input("Enter the side of the square: "))
for i in range(1,n+1):
    fact=fact*i
print("The total number of routes is: ",fact*fact)
