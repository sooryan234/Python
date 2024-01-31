print("RECTANGLE")
print("................")
l=float(input("Enter length:"))
b=float(input("Enter breadth:"))
perimeter=lambda l,b:2*(l+b)
print("perimeter is",perimeter(l,b))
area=lambda l,b:l*b
print("Area is",area(l,b))
print("SQUARE")
print(".....................")
a=float(input("Enter the side:"))
perimeter=lambda a:4*a
print("Perimeter:",perimeter(a))
area=lambda a:a*a
print("Area is",area(a))
