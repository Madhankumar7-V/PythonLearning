arr=list(map(int,input("Enter Numbers : " ). split()))
key=int(input("Enter the element to search : "))
num=len(arr)
found=False

for i in range(num):
    if key==arr[i]:
        print("Element found at index",i)
        found=True
        break
else:
    print("Element Not found")
              
