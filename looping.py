# -*- coding: utf-8 -*-
"""
Created on Wed May 27 15:27:42 2026

@author: ASUS
"""

range(10)
list(range(10))
list(range(5,21))
list(range(5,50,5))
list(range(5,51,5))
list(range(51,5,-5))
list(range(50,5,-5))
list(range(50,4,-5))

for i in range(10):
    print("Shivatmika")
    
    
    
n=int(input("Enter the number of time the name has to be displayed"))
for i in range(n):
    print("Shivatmika")
    
    
    
for i in range(1,10,-1):
    print(i)   
    
    
    
for i in range(10,1,-1):
    print(i)   
    
    
    
for i in range(10,0,-1):
    print(i)    
    
    
    
    
    
n=int(input("Enter the number of even numbers to be displayed: "))
for i in range(2,(2*n)+1,2):
    print(i)



n=int(input("Enter the how many odd numbers are to be displayed: "))
for i in range(1,(2*n)+1,2):
    print(i)
    
    
    
sum=0
for i in range(10):
    sum+=i
print(sum)



sum=0
for i in range(11):
    sum+=i
print(sum)



s=0
for i in range(50):
    n=int(input("Enter the number: "))
    s+=n
print(s)



se=0
so=0
for i in range(50):
    n=int(input("Enter the number: "))
    if n%2==0:
        se+=n
    else:
        so+=n



sp=sn=0
while True:
    n=int(input("Enter the number: "))
    if n>0:
        sp+=n
    elif n<0:
        sn+=n
    else:
        break
print("Sum of Positive numbers",sp)
print("Sum of Negative numbers",sn)

 

avg=sum=c=0
while True:
    n=int(input("Enter the number: "))
    if n!=0:
        sum+=n
        c+=1
    else:
        break
avg=sum/c
print("The sum of all numbers:",sum)
print("The average of all the numbers is:",avg)



max=min=n=int(input("Enter the number:"))
while True:
    if n==0:
        break
    if n>max:
        max=n
    if n<min:
        min=n
    
    print('Maximum:',max,'  Minimum:',min)
    n=int(input("Enter the number:"))
    
    
    
n=int(input("Enter the number:"))
for i in range(1,11):
    print(n,"x",i,"=",n*i)
    


for i in range(65,91):
    print(chr(i),i)           #ASCII



m=int(input("Enter the month number:"))
d=int(input("Enter in day:"))
y=int(input("Enter the year:"))
sum=d
for i in range(1,m):
    if i in [1,3,5,7,8,10,12]:
        sum+=31
    elif i in [4,6,9,11]:
        sum+=30
    else:
        if y%400==0 or (y%100!=0 and y%4==0):
            sum+=29
        else: 
            sum+=28
print("The number of day tha have passed in this year:",sum)



n=int(input("Enter the number: "))
if (n%7==0) and (n%10==7):
    print("It is a buzz number")
else:
    print("It is not a buzz number")
    
    
    
n=int(input("Enter the number:"))
if (n**0.5)%1==0:
    print("It is a Perfect Square")
else:
    print("It is not a Perfect Square")
 
    
 
n=int(input("Enter the number:"))
if ((n+1)**0.5)%1==0:
    print("It is a Sunny number")
else:
    print("It is not a Sunny number")



n=int(input("Enter the number:"))
sum=0
for i in range(1,n+1):
    if(n%i==0):
        sum+=i
print("The sum of all the factors is",sum)



n=int(input("Enter the number:"))
sum=0
for i in range(1,n):
    if(n%i==0):
        sum+=i
if(n==sum):
        print("It is a perfect number")
else:
        print("It is not a perfect number")
        
        
        
n=int(input("Enter the number:"))
sum=0
for i in range(1,n):
    if(n%i==0):
        sum+=i
if(n<sum):
        print("It is a abundant number")
else:
        print("It is not a abundant number")        


        
n=int(input("Enter the number:"))
sum=0
for i in range(1,n):
     if(n%i==0):
         sum+=i
if(n>sum):
         print("It is a deficient number")
else:
         print("It is not a deficient number")      

   

n=int(input("Enter the first number:"))
m=int(input("Enter the second number:"))
sn=sm=0
for i in range(1,n):
    if(n%i==0):
        sn+=i
for i in range(1,m):
    if(m%i==0):
        sm+=i
if(sn==m and sm==n):
    print("Ther are ambicable numbers")
else:
    print("They are not ambicable number")
    
    
    
n=int(input("Enter the number:"))
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1
        print(i)
print("The number of factors",count)



n=int(input("Enter the number:"))
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1
if count==2:
    print("It is a Prime Number")
else:
    print("It is no a prime number")



n=int(input("Enter the first number:"))
m=int(input("Enter the second number:"))
cn=cm=0
for i in range(1,n+1):
    if n%i==0:
        cn+=1
for i in range(1,m+1):
    if m%i==0:
        cm+=1 
if (cn==2 and cm==2 and abs(m-n)==2):
    print("They are twin prime numbers")
else:
    print("They are not twin prime numbers")
    
    
    
n=int(input("Enter the number: "))
while True:
    n+=1
    cn=0
    for i in range(1,n+1):
        if n%i==0:
            cn+=1
    if cn==2:
        print("The next prime number is:",n)
        break
        
    
    
n=int(input("Enter the first number: "))#75
m=int(input("Enter the second number: "))#100

lcm=max(m,n)
while not(lcm%m==0 and lcm%n==0):
    lcm+=1
print(lcm)



num=n=int(input('Enter the number for prime factorization:'))
i=2
while n!=1:
    if n%i==0:
        print(i,end='')
        n/=i
        if n!=1:
            print(end=' x ')
    else:
        i+=1
print(' =',num)



nn=n=int(input("Enter the first number:"))
mm=m=int(input("Enter the second number:"))
i=2
lcm=1
print('-'*22)
while n!=1 or m!=1:
    print(f"{i:>2} | {n:>5}   ,   {m:>5}")
    print('-'*22)
    if n%i==0 and m%i==0:
        n//=i
        m//=i
        lcm*=i
    elif n%i==0:
        n//=i
        lcm*=i
    elif m%i==0:
        m//=i
        lcm*=i
    else:
        i+=1
print('LCM of',nn,'and',mm,'is',lcm)
        



n=int(input("Enter the first number:"))
m=int(input("Enter the second number:"))
i=2
lcm=1
while n!=1 or m!=1:
    if n%i==0 or m%i==0:
        if n%i==0:
            n/=i
        if m%i==0:
            m/=i
        lcm*=i
    else:
        i+=1
print(lcm)
    


n=int(input("Enter the first number:"))
m=int(input("Enter the second number:"))
i=2
hcf=1
while n!=1 or m!=1:
    if n%i==0 and m%i==0:
        n/=i
        m/=i
        hcf*=i
    elif n%i==0:
        n/=i
    elif m%i==0:
        m/=i
    else: 
        i+=1
print(hcf)


n=int(input("Enter the number to be checked: "))
i=2
while n>1 and i<=5:
    if n%i==0:
        n/=i
    else:
        i+=1
if i<=5:
    print("It is a ugly number")
else:
    print("It is not a ugly number")
    
    
    
    
    
    














