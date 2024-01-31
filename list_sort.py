n=int(input("Enter the size of list:"))
a=[]
for i in range(n):
    e=input("Enter the elemnt:")
    a.append(e)
print("Before sorting:",a)
a.sort()
print("after sorting:",a)
