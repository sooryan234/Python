a=input("Enter first number:")
b=input("Enter second number:")
c=input("Enter third number:")
if a>b and a>c:
    print(a,"is largest")
elif b>c and b>a:
    print(b,"is largest")
else:
    print(c,"is largest")
