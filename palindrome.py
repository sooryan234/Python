def palindrome(n):
    rev=0
    temp=n
    while(n>0):
        rem=n%10
        rev=(rev*10)+rem
        n=n//10
    if(temp==rev):
     return temp
n=int(input("Enter a number:"))
result=palindrome(n)
if(result==n):
    print(n,"is palindrome")
else:
     print(n,"is not palindrome")
    
