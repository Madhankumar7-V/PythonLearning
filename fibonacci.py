num=[0,1]
fibo=[0,1]
for i in range(10):
    result=num[i]+num[i+1]
    num.append(result)
    fibo.append(result)
print(fibo)
    
