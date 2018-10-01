#0041 Temp Conversion

def celsius(f):
    ans=5/9*(f-32)
    print("fahrenheit to celsius= ",ans)
def fahrenheit(c):
    ans=(9/5*c)+32
    print("celsius to fahrenheit= ",ans)

f=float(input("Enter temperature in fahrenheit: "))
c=float(input("Enter temperature in celsius: "))

celsius(f)
fahrenheit(c)

