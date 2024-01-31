a=float(input("Enter the first number:"))
b=float(input("Enter the second number:"))
optr=input("Enter an operator(+,-,*,/,%,**,//):")
if(optr=="+"):
    r=a+b
elif optr=="-":
    r=a-b
elif optr=="*":
    r=a*b
elif optr=="/":
    r=a/b
elif optr=="**":
    r=a**b
elif optr=="%":
    r=a%b
elif optr=="//":
    r=a//b
else:
    print("Enter a valid operator!!")
print("The result is:",r)
