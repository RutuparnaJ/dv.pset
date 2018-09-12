#1000 digit fibonacci number index=4782
a=1
b=1
c=0
num=0
rem=0
count=0
digits=0

while digits<1000:
    c=a+b
    print(c)
    a=b
    b=c
    num=c
    count=count+1
    digits=0
    while(num>=1):
        digits=digits+1
        rem=(num%10)
        num=(num//10)
    if(digits==1000):
        break
    
        
print("Index: ",count+2)  #count+2 accounts for F1 nd F2 =1
   
