a=int(input("Enter the first number"))
b=int(input("Enter the second number:"))
print("With temporary variables")
print("a before swapping:",a)
print("b before swapping:",b)
temp=a
a=b
b=temp
print("a before swapping:",a)
print("b before swapping:",b)
print("Without temporary variables")
print("a before swapping:",a)
print("b before swapping:",b)
a=a+b
b=a-b
a=a-b
print("a before swapping:",a)
print("b before swapping:",b)
