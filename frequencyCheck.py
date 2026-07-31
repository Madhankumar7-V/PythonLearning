arr=list(map(int, input("Enter numbers : ").split()))
key=int(input("Enter Number to check frequency : "))
count=0

for i in arr:
    if i==key:
        count+=1
print("Frequency : ",count)
