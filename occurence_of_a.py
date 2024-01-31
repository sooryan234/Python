str=input("Enter a string:")
count=0
for i in range(len(str)):
    if str[i]=="a":
        count=count+1
print("The number of 'a' in the word",str,"is:",count)
