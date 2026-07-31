Subject = int(input("Enter number of Subjects : "))
print("Enter Marks for the subjects out of 100 Only")
marks=[]
for i in range(Subject):
    mark=int(input(f"Enter Subject {i+1} Marks : "))
    marks.append(mark)

total=sum(marks)
grade=(total/Subject*100)*100
print(round(grade,3))
    
                    
