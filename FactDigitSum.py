#0066 Factorial Digit Sum
import math 
fact=1
Sum=0
for i in range(1,11):
    fact=fact*i

print("The factorial of 100 is: ", fact)
while(fact>0):
    rem=int(fact%10)
    fact=int(fact/10)
    Sum=Sum+rem
print(Sum)
