n=int(input("Enter a number : "))
if n==0 or n==1:
    print("Not Prime")
elif n<0:
    print("Cannot Check for Negative Numbers")
    print("Try with a Positive Number")
else:
    for i in range(2,n):
        if n%i==0:
            print("Not Prime")
            break
    else:
        print(f"{n} Its a Prime Number")
