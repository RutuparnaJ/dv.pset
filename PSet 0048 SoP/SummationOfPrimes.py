#0048 Summation of Primes ans: 142913828922
import math 
Sum=0
num=2
i=0
count=0
while num<2000000:
    count=0
    for i in range(2,int(math.sqrt(num))+1): #range is only till square root to decrease run time.
        if num%i==0:
            count=count+1 #if num has divisors other than 1 or num itself, the counter will increase
    if count==0: #if no divisors, it is prime
        print(num)
        Sum=Sum+num  #addition of prime
    num=num+1
print("Sum= ",Sum)
