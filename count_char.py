str=input("Enter a string:")
count=0
n=len(str)
for i in range(n):
    if(str[i]!=' '):
        count=count+1
print("The number of characters in",str,"is",count)
