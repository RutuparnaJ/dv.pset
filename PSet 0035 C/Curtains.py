#0035 Curtains
i=0
count=0
arr=[]
word=str(input("Enter a word: "))
for i in word:
    arr.append(i)
    count=count+1
for i in range(count):
    for j in range(i+1):
        print(arr[j],end="")
        i=i+1
    print()
