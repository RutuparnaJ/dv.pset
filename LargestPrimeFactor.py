#largest prime factor
i=0
pfact=0
for i in range(1,22):
    if(22%i==0):
        print ("i= ",i)
        for fact in range(2,i+1):
            if(i%fact!=0):
                pfact=fact
                print ("pfact= ",pfact)

print (pfact) 
        
