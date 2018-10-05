#0080 ReverseSum

def reverse_sum_and_check_equality(x):
    rem=0
    Sumx=0
    Sumrev=0
    rev = x[::-1]
    print(x,rev)
    x=int(x)
    rev=int(rev)
    while x!=0:
         rem= x%10
         x= x//10
         Sumx= Sumx+rem
    rem=0
    while rev!=0:
         rem= rev%10
         rev= rev//10
         Sumrev= Sumrev+rem

    if Sumrev==Sumx:
        print("True")
    else:
        print("False")
    

x=str(input("Enter a number: "))
reverse_sum_and_check_equality(x)

    
