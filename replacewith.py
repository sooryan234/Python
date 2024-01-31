str=input("Enter a string:")
f=str[0]
new=f+str[1:].replace(f,"$")
print("The new string is:",new)
