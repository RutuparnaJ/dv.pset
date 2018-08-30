#largest prime factor
i=0
pfact=0
count=0
for i in range(2,13195):
    if(13195%i==0):   #finding factors 
        #print ("i= ",i)
        count=0
        for fact in range(2,i): #checking whether factor is prime
            if(i%fact!=0):
                count=count+1
            if(count==i-2):
                pfact=i
                print ("pfact= ", pfact)

print ("The largest prime number is: ",pfact) 
        
