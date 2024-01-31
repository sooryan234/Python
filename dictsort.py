student={}
n=int(input("Enter the size:"))
for i in range(n+1):
    name=input("Enter the name:")
    age=int(input("Enter the age:"))
    student[name]=age
print("before sorting:",student)
lst=list(student.items())
lst.sort()
student=dict(lst)
print("After sorting:",student)
lst.sort(reverse=True)
student=dict(lst)
print("After reverse:",student)    
