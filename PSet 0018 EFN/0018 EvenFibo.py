#0018 Even fibonacci numbers
a=1
b=1
c=a+b
Sum=0
while(c<4000000):
    c=a+b
    a=b
    b=c
    if(c%2==0):
        print(c)
        Sum=Sum+c
print(Sum)
