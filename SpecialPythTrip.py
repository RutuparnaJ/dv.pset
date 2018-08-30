#Special Pythagorean triplet
#
c=3
b<c
a<b
a>0







for c in range (3,1000):
    if a*a + b*b == c*c and a + b + c == 1000:
        print(a, b, c)
