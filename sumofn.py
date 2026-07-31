n=int(input("Enter Number of Elements to Sum : "))
add=[]
for i in range(n):
    ele=int(input(f"Enter Element {i+1} : "))
    add.append(ele)
print("Sum = : ",sum(add))
