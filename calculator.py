n1=int(input("Enter first number:"))
n2=int(input("Enter second number:"))
optr=input("Enter any operator:")
def add(n1,n2):
    r=n1+n2
    return r
def sub(n1,n2):
    r=n1-n2
    return r
def mul(n1,n2):
    r=n1*n2
    return r
def sub(n1,n2):
    r=n1/n2
    return r
def calc(n1,optr,n2): 
   if optr=="+":
      return add(n1,n2)
   elif optr=="-":
     return sub(n1,n2)
   elif optr=="*":
      return mul(n1,n2)
   elif optr=="/":
      return div(n1,n2)
   else:print("invalid")
print("result is:",calc(n1,optr,n2))
    
