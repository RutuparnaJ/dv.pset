# 0052 Longest Collatz Sequence
n=0
num=0
count=1
large=0
for i in range(2,20):
    n=i
    print("i=",i)
    count=1
    
    while n>=1:
        #print("n=",n)
       
        if n%2==0:
            n=n//2
            #print("even ",n)
            count=count+1
            if n==1:
                print("count= ",count)
                if count>large:
                    large=count
                    num=i
                break
        
        if n%2!=0:
            n=3*n+1
            #print("odd ",n)
            count=count+1
    
      
            
print("num= ", num,"i= ",i, "large=",large)
