#0070 lexicographic permutations
#Most of the print statements are for verification
i=0
j=0
num=0
r=10
count=0
arr=[0,1,2,3,4,5,6,7,8,9]
fact=[362880,40320,5040,720,120,24,6,2,1,1]#array of factorials. eg the first digit will change every 9!

for i in range (10):
    for j in range (10):
        if num+fact[0]*j<=1000000: #makes sure the number does not exceed 1M
             if 1000000-(num+fact[0]*j)<fact[0]:#makes sure the largest multiple of the current fatorial is used
                         num=num+fact[0]*j #updates the number
                         count=count+fact[0]*j
                         break
    if i<9 and count==1000000: #makes sure that the millionth permutation is reached only at the last digit
        j=j-1
    print("plus prev ",arr[j], " j= ",j) #prints each digit with each iteration starting with the leftmost
    arr.pop(j) # removes the value of j from the array to prevent repetition
    fact.pop(0) # removes the first value of the factorial array as the number increases
    r=r-1 #just for printing, prevents index list out of range msg
    print("new array:")
    for j in range(r):
        print(arr[j],end=" ")
    print("new fact array:")
    for i in range(r):
        print(fact[i],end=" ")
    print("count= ",count)
