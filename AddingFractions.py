#Adding Fractions
NewDen=1
NewNum=1
num1=int(input("Enter the numerator of the first fraction: "))
den1=int(input("Enter the denominator of the first fraction: "))
num2=int(input("Enter the numerator of the second fraction: "))
den2=int(input("Enter the denominator of the second fraction: "))
print("The two fractions entered are: ", num1,"/",den1, " and ", num2,"/",den2)
NewDen=den1*den2
NewNum=num1*den2 + num2*den1
print("The added fraction is: ", NewNum,"/",NewDen)
