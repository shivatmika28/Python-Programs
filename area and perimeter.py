side=int(input("Enter the side of square"))
print("The perimeter of square of side",side,"is",side*4)
print("The area of square of side",side,"is",side**2,end='\n\n')

l=int(input("Enter the length of rectangle"))
b=int(input("Enter the breadth of rectangle"))
print("The perimeter of rectangle of length",l,"and breadth",b,"is",2(l+b))
print("The area of rectangle of length",l,"and breadth",b,"is",l*b)

s1=int(input("Enter the 1st side of triangle"))
s2=int(input("Enter the 2nd side of triangle"))
s3=int(input("Enter the 3rd side of triangle"))
print("The perimeter of triangle of sides is",s1+s2+s3)
s=(s1+s2+s3)/2
print("The area of triangle of sides is",((s*(s-s1)*(s-s2)*(s-s3))**0.5))

r=int(input("Enter the radius of circle"))
print("The circumference of circle of radius",r,"is",2*(22/7)*r)
print("The area of circle of radius",r,"is",(3.14)*r**2)

cs=int(input("Enter the side of cube"))
print("The surface area of cube of side",cs,"is",6*cs**2)
print("The volume of cube of side",cs,"is",cs**3)

cl=int(input("Enter the length of cuboid"))
cb=int(input("Enter the breadth of cuboid"))
ch=int(input("Enter the height of cuboid"))
print("The surface area of the cuboid is",2*(l*b+b*h+h*l))
print("The volume of cuboid of side",l*b*h)

