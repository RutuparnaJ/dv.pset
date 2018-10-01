#0040 Calculator
ans=0

def add(x,y):
    ans=x+y    
    print("Sum= ",ans)
def subtract(x,y):
    ans=x-y
    print("Difference= ",ans)
def multiply(x,y):
    ans=x*y
    print("Product= ",ans)
def divide(x,y):
    ans=x/y
    print("Quotient= ",ans)

print("Enter two numbers: ")
x=int(input())
y=int(input())


add(x,y)
subtract(x,y)
multiply(x,y)
divide(x,y)


