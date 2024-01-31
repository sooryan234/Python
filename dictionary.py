student={}
n=int(input("Enter the number of elements in dictionary:"))
for i in range(n+1):
    name=input("Enter the name:")
    grade=input("Enter the grade:")
    student[name]=grade

print(student)
