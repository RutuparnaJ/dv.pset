#0079 Reverse
x=0
rev=0
def reverseNumber(x):
    while x>0:
        rev=x%10
        x=x//10
        print(rev, end="")

x=int(input("Enter a number: "))

reverseNumber(x)
    
        
