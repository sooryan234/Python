n=int(input("Enter number of elements in the list:"))
a=[]
for i in range(n):
    e=input("Enter the element:")
    a.append(e)
print("list is:",a)
max=len(a[0])
temp=a[0]
for i in a:
    if(len(i)>max):
        max=len(i)
        temp=i
        print("length of largest word is:",max,"largest word is",temp);
