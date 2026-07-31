arr=list(map(int,input("Enter Numbers : ").split()))

odd=0
even=0

for i in range(len(arr)):
    if arr[i]%2==0:
        even+=1
    else:
        odd+=1
print("Odd : ",odd)
print("Even : ",even)
