#Sigma fuction
#S1= n+1
#S2= n+2
#S3!=n^2
import math
S1=0
S2=0
S3=0
n= int(input("Enter a number: "))
for i in range (1,n+1):
    S1= int(S1+i)
    if i%2!=0:
        S2=int(S2+i)
    if math.sqrt(i)!=int(math.sqrt(i)):
        S3=int(S3+i)
    
print("S1=", S1, " S2=", S2, " S3=", S3)    

