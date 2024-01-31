str=input("Enter a string:")
n=len(str)
f=str[0]
l=str[n-1]
new=l+str[1:].replace(l,f)
print(new)
