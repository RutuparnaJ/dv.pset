#Linear Search

arr = [1, 2, 5, 7, 10, 21, 27, 30, 41, 53, 61]

i=0
count=0
search= int(input("Enter the number to be searched: "))
for i in range (0,10):
    if(search==arr[i]):
        count=1
        print("Number found! Index = ", i)
if count==0:
    print("Sorry, number not found")
    

