#PSet 0057 Consecutive numbers
i=0
row=1
column=1
n=int(input("Enter a number "))
 
for i in range(1,n+1):
    if(row==column):    #checking whether the row and column coordinates are equal
        print(i)         
        column=1        #resetting the column value to 1
        row=row+1       #incrementing row for next line
    else:
        print(i, end=" ") #printing i and keeping cursor for next number on the same line
        column=column+1     #incrementing column value
