n=int(input("Enter a Number : "))

temp=n
digits=len(str(n))
sum=0

while temp>0:
    digit=temp%10
    sum+=digit**digits
    temp//=10

if sum==n:
    print("Armstrong Number")
else:
    print("Not a Armstrong Number")
