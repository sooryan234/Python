n=input("Enter a binary number:")
decimal=0
for i in range(0,len(n)):
    digit=int(n[i])
    decimal=decimal+digit*2**(len(n)-i-1)
print("Decimal equivalent of",n,"is",decimal)
