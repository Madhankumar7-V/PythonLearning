arr=[]
for i in range(1,4):
    num=int(input(f"Enter Number {i} : "))
    arr.append(num)
if (arr[0]>arr[1]):
    if(arr[0]>arr[2]):
        print("Greatest Number : ",arr[0])
    else:
        print("Greatest Number : ",arr[2])
elif (arr[1]>arr[2]):
    print("Greatest Number : ",arr[1])
else:
    print("Greatest Number : ",arr[2])
