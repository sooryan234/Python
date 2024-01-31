n=int(input("Enter the number:"))
e=int(input("Enter the exponent:"))
def power(n,e):
    if(e==0):
        return 1
    elif(e==1):
        return n
    else:
        return n*power(n,e-1)
print(n,"raised to power of",e,"is:",power(n,e))
