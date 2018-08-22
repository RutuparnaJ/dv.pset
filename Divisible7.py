# Is divisible by 7?
i=1
j=0
n=int(input("Enter a number: "))
for i in range (1,n):
    if i%7==0:
        j=j+1
print(j)
