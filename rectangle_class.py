class rect():
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def perimeter(self):
        return 2*(self.l+self.b)
    def area(self):
        return self.l*self.b
l=float(input("Enter the length:"))
b=float(input("Enter the breadth:"))
obj=rect(l,b)
print("Area is:",obj.area())
print("Perimeter is:",obj.perimeter())
