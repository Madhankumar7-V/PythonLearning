num=int(input("Enter a Number : "))
if(num<0):
    print("factorial doesn't exist for negative numbers")
elif(num==0 or num==1):
    print("Factorial = 1 ")
else:      
    fac=1
    for i in range(1,num+1):
        fac=fac*i
    print("Factorial = ",fac)
    
