#0024 10001st Prime = 104743
import math
n=2
i=0

count=0
prime=0
while n>0:
    count=0
    for i in range(2, int(math.sqrt(n)+1)):
        if n%i==0:
            count=count+1
    if count==0:
        prime=prime+1
        print("pn ",n)
    if prime==10001:
        print("10001th prime: ",n)
        break
    n=n+1
        
