#sum of digits
Sum=0
num=int(input('Enter the number whose sum of digits you want to find: '))
while num!=0:
     rem= num%10
     num= int(num/10)
     Sum= Sum+rem
print('The sum is: ',Sum)
