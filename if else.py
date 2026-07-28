s=int(input("Enter the time in seconds:"))
h=s//3600
s%=3600
m=s//60
s=s%60
print("Time taken: ",h,"hr",m,"min",s,"sec")



'''DECISION MAKING PROGRAMS '''




age=int(input("Enter the age of the user:"))
if age>=18:
    print("You can vote")
else:
    print("You cannot vote")    



n1=int(input("Enter the first number:"))
n2=int(input("Enter the second number:"))
if n1>n2:
    print(n1,"is greater than",n2)
elif n2>n1:
    print(n2,"is greater than",n1)
else:
    print("Both are equal")

    
    
d1=int(input("Enter the first digit: "))
d2=int(input("Enter the second digit: "))
d3=int(input("Enter the third digit: "))
ma=max([d1,d2,d3])
mi=min([d1,d2,d3])
md=(d1+d2+d3)-(ma+mi)
print("The largest number is",ma*100+md*10+mi)
print("The smallest number is",mi*100+md*10+ma)



c=input("Enter the character: ")
if len(c)>1:
    print("Invalid")
else:
    if (c>='A' and c<='Z') or (c>='a' and c<='z'):
        print("Yes")
    else:
        print("No")
        
        
        
d=input("Enter the character: ")
if len(d)>1:
    print("Invalid")
else:
    if d>='0' and d<='9':
        print("No")
    else:
        print("Yes")
        
        
        
c=input("Enter the character: ")
if c in 'aeiouAEIOU':
    print("It is a vowel")
else:
    print("It is not a vowel")
    
    
    
c=input("Enter the character:")
if (c not in 'aeiouAEIOU') and ((c>='A' and c<='Z') or (c>='a' and c<='z')):
    print("It is a consonent")
else:
     print("It is not a consonent")
     
     
     
c=input("Enter the character: ")
if  c.isupper() :
    print("Character is in Uppercase")
else:
    print("It is not in Uppercase")



c=input("Enter the character: ")
if  c.islower() :
    print("Character is in Lowercase")
else:
    print("It is not in Lowecase")
    
    
    
c=int(input("Enter the month number: "))
d=0
if c in [4,6,9,11]:
    d=30 
elif c in [1,3,5,7,8,10,12]:
    d=31
else:
    y=int(input("Enter the year: "))
    if y%400==0 or (y%100!=0 and y%4==0):
        d=29
    else: 
        d=28
print("The number of days in this month is",d)



c=input("Enter the month name: ")
c=c.lower()
if c in ["december","january","february"]:
    print("Winter")
elif c in ["march","april","may"]:
    print("Summer")
elif c in ["june","july","august","september"]:
    print("Rainy")
else:
    print("Autum")
    
    
    
print('''******Menu******
1.Sum
2.Difference
3.Product
4.Quotient
5.Remainder''')
n=int(input("Enter the choice:"))
n1=int(input("Enter the first number:"))
n2=int(input("Enter the second number:"))
if n==1:
    print("The Sum of",n1,"and",n2,"is",n1+n2)
elif n==2:
    print("The difference of",n1,"and",n2,"is",n1-n2)
elif n==3:
    print("The Product of",n1,"and",n2,"is",n1*n2)
elif n==4:
    print("The Quotient of",n1,"and",n2,"is",n1/n2)
elif n==5:
    print("The Remainder of",n1,"and",n2,"is",n1%n2)
    
    
    
w=float(input("Enter your weight in kg:"))
h=float(input("Enter your height in meters:"))
bmi=w/(h**2)
print(bmi)
if bmi<18.5:
    print("Underweight")
elif bmi>=18.5 and bmi<=24.9:
    print("Healthy Weight")
elif bmi<=25.0 and bmi>=29.9:
    print("Overweight")
else:
    print("Obese")



a=int(input("Enter the first side of triangle:"))
b=int(input("Enter the second side of triangle:"))
c=int(input("Enter the third side of triangle:"))
if a+b>c and b+c>a and c+a>b and a!=b and b!=c and c!=a:
    print("The trianlge is possible and it is scalene.")
else:
    print("The triangle is not possible")
    
    
    
a=int(input("Enter the first side of triangle:"))
b=int(input("Enter the second side of triangle:"))
h=int(input("Enter the third side of triangle:")) 
if a+b>h and b+h>a and h+a>b:
    if (a**2)+(b**2)==(h**2):
        print("It is a right angle triangle")
    elif (a**2)+(b**2)<(h**2):
        print("It is a acute angle triangle")
    elif (a**2)+(b**2)>(h**2):
        print("It is a obtuse angle triangle")
        
        
        
    '''LOOPING PROGRAMS '''   
    p