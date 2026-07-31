arr=list(map(int, input("Enter Numbers : " ).split()))

total=0
Maximum=arr[0]
Minimum=arr[0]

for i in arr:
    total+=i

    if Minimum>i:
        Minimum=i
    if Maximum<i:
        Maximum=i

average=total/len(arr)

print(total)
print(Minimum)
print(Maximum)
print(average)
