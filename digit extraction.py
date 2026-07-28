n=int(input("Enter the number:"))  #python way
for i in str(n):    #n=983  str(n) -> '983'
    print(i)
    
    
    
n=int(input("Enter the number: ")) #reverse
for i in str(n)[::-1]: #start stop step 
    print(i)
    


n=int(input("Enter the number:"))  #java way 
while n>0:
    print(n%10)
    n//=10
    
    

#largest digit and smallest  
n=int(input("Enter the number: ")) #not for just 0 
ma=-1
mi=10
while n>0:
    d=n%10
    if ma<d:
        ma=d
    if mi>d:
        mi=d
    n//=10
print("The largest digit is:",ma)
print("The smallest digit is:",mi)




#easy way using function 
n=int(input("Enter the number: "))
print("The largest digit is:",max(str(n)))
print("The smallest number is:",min(str(n)))




#total number of digits
n=int(input("Enter the number: "))
c=0
while n>0:
    d=n%10
    n//=10
    c+=1
print("The total number of digits are:",c)



n=int(input("Enter the number: "))
print("The total number of digits are:",len(str(n)))



#sum of number = no of digits in number
n=int(input("Enter the number: "))
c=len(str(n))
sum=0
for i in str(n):   #different logic
    sum+=int(i)
if c==sum:
    print("It is a SUPERSPY number")
else:
    print("It is not a SUPERSPY number")
    
    


#sum of all digits except the last digit = last digit
n=int(input("Enter the number: "))
sum=0
for i in str(int(n/10)):
    sum+=int(i)
if n%10==sum:
    print("It is a HANDSOME number")
else:
    print("It is not a HANDSOME number")
    
    
    
    
#the sum of digits of the square of the number = number
n=int(input("Enter the number: "))
sum=0
for i in str(n*n):
    sum+=int(i)
if(n==sum):
    print("It is a NEON number")
else:
    print("It is not a NEON number")
    
    
    
    
#product of all digits
n=int(input("Enter the number: "))
prod=1
for i in str(n):
    prod*=int(i)
print("The product of all digits",prod)




#(sum+product)of digits = number itself
n=int(input("Enter the number: "))
sum=0
prod=1
for i in str(n):
    sum+=int(i)
    prod*=int(i)
if sum+prod==n:
    print("It is a SPECIAL TWO DIGIT number")
else:
    print("It is not a SPECIAL TWO DIGIT number")
    
    


#sum of digits = prod of digits
n=int(input("Enter the number: "))
sum,prod=0,1
for i in str(n):
    sum+=int(i)
    prod*=int(i)
if sum==prod:
    print("It is SPY number")
else:
    print("It is not a SPY number")
    
    


#the product of the sum of digits and product of digits = the number itself
n=int(input("Enter the number too be checked: "))
sum=0
prod=1
for i in str(n):
    sum+=int(i)
    prod*=int(i)
if(sum*prod==n):
    print("It is a SUM-PRODUCT number")
else:
    print("It is not a SUM PRODUCT number")



#(sum of digits)^3 = the number itself
n=int(input("Enter the number to be checked: "))
sum=0
for i in str(n):
    sum+=int(i)
if(sum**3==n):
    print("It is a DUDENEY number")
else:
    print("It is not a DUDENEY number")


#number is divisible by sum of its digits 
n=int(input("Enter the number to be checked: "))
sum=0
for i in str(n):
    sum+=int(i)
if(n%sum==0):
    print("It is a HARSHAD number")
else:
    print("It is not a HARSHAD number")


#(digits)^3+(digit)^3=sum , this sum = number itself
n=int(input("Enter the number to be checked: "))
sum=0
c=len(str(n))
for i in str(n):
    sum+=int(i)**c
if (sum==n):
    print("It is a ARMSTRONG number")
else:
    print("It is not a ARMSTRONG number")



#(digit)^its position ka sum = number itself
n=int(input("Enter the number to be checked"))
sum=0
pos=1
for i in str(n):
    sum+=int(i)**pos
    pos+=1
if(sum==n):
    print("It is a DISARIUM number")
else:
     print("It is not a DISARIUM number")   
     


n=int(input("Enter the number:"))       #question 18 and 19
sum=0
for i in str(n):
    f=1
    for j in range(1,int(i)+1):
        f*=j
    sum+=f
print("Sum of factorial of its digits is:",sum)



n=int(input("Enter the number: "))
esum=osum=0
for i in str(n):
    if int(i)%2==0:
        esum+=int(i)
    else:
        osum+=int(i)
print("The sum of digits is",esum,"sum of odd digits",osum)
if esum==osum:
    print("It is a LEAD number")
else:
    print("It is not a LEAD number")
    
    
    
n=int(input("Enter the number: "))
ec=oc=0
for i in str(n):
    if int(i)%2==0:
        ec+=1
    else:
        oc+=1
print("The number of even digits are",ec,"and the number of odd digits",oc)        



n=int(input("Enter the number: "))#n=25
sq=n**2                             #sq=625
c=len(str(n))
last_digit=sq%(10**c)
if last_digit==n:
    print("It is an AUTOMORPHIC number")
else:
    print("It is not an AUTOMORPHIC number")



n=int(input("Enter the number: "))
cub=n**3
c=len(str(n))
last_digit=cub%(10**c)
if last_digit==n:
    print("It is an TRIMORPHIC number")
else:
    print("It is not an TRIMORPHIC number")
    
    

n=int(input("Enter the number: "))
c=0
for i in str(n):
    if(int(i)==0):
      c+=1
print("The number of zeros in",n," number is ",c)



#1st logic
n=int(input("Enter the number: "))
check=0
for i in str(n):
    if(int(i)==0):
      check=1
      break
    else:
        check=0
if check==1:
    print("It is a DUCK number")
else:
    print("It is not a DUCK number")
    
    
    
#2nd logic
n=int(input("Enter the number: "))
for i in str(n):
    if(int(i)==0):
      break
if i=='0':
    print("It is a DUCK number")
else:
    print("It is not a DUCK number")
    
    
    
#3rd logic
n=int(input("Enter the number: "))
if '0' in str(n):
    print("It is a DUCK number")
else:
    print("It is not a DUCK number")
    
    
    
    
n=int(input("Enter the number to be checked: "))
flag=True
for i in str(n):        
    if str(n).count(i)!=1:
        flag=False
        break
if flag==True:
    print("It is a UNIQUE number")
else:
    print("It is not a UNIQUE number")
    


n=int(input("Enter the number to be checked(the number should be even): "))
c=len(str(n))
p=n//(10**(c//2))
q=n%(10**(c//2))         
sum=p+q
if(sum**2==n):
    print("It is a TECH number")
else:
    print("It is not a TECH number")
    
    
    
n=int(input("Enter the number to be checked: "))
c=len(str(n))
if c%2==0:
    c=len(str(n))
    p=n//(10**(c//2))
    q=n%(10**(c//2))
    print("The first number is",p)
    print("The second digit is",q)
else:
    print("The middle digit is",(n//10**(c//2))%10)
    
    
    
    
n=int(input("Enter the number to be checked:")) 
if n==int(str(n)[::-1]):
    print('Yes')
else:
    print('No')


n=int(input("Enter the number to be checked:"))
copy=n
rev=0
while copy>0:
    rev=rev*10+copy%10
    copy//=10
if n==rev:
    print('Yes it is a Pallindrome')
else:
    print('No it is not a Pallindrome')



n=int(input("Enter the number to be checked:")) 
while n>9:            #1252
    s=0
    for i in str(n):
        s+=int(i)
    n=s
        
if n==1:
    print("It is a MAGIC number")
else:
   print("It is not a MAGIC number") 
   
   
   
n=int(input("Enter the number to be checked:")) 
while n!=1 and n!=4:
    s=0
    for i in str(n):
        s+=int(i)**2
    n=s
if n==1:
    print("It is a HAPPY number")
else:
    print("It is a NON HAPPY number")
    
    
    
n=int(input("Enter the number to be checked: "))  
while n>9:
    s=0
    for i in str(n):
        s+=int(i)**2
    n=s
if n!=1:
    print("It is an UNHAPPY number")
else:
    print("It is not an Unhappy number")
    

#question 5-smith number
def sumofdigits(n):
    s=0
    for i in str(n):
        s+=int(i)
    return s

a=n=int(input("Enter the number to be checked: "))
i=2
s=0
while n>1:
    if n%i==0:
        n/=i
        s+=sumofdigits(i)
    else:
        i+=1
if s==sumofdigits(n):
    print("It is a Smith number")
else:
    print("It is not a Smith number")
        
    
        
    
n=int(input("Enter the number to be checked: "))    
s=str(n)
if s.find('0')>=0 and s.find('1')>=0 and s.find('2')>=0 and s.find('3')>=0 and s.find('4')>=0 and s.find('5')>=0 and s.find('6')>=0 and s.find('7')>=0 and s.find('8')>=0 and s.find('9')>=0:
    print("It is a PANAGRAM number")
else:
    print("It is not a PANAGRAM number")
    


n=int(input("Enter the number to be checked: "))    
s=str(n)
num='0123456789'
flag=True
for i in num:
    if i not in s:
        flag=False
        break
if flag:
    print("It is a PANAGRAM number")
else:
    print("It is not a PANAGRAM number")
    
    
    
    
#largest to smallest(using looping)
n=int(input("Enter the number to be converted into largest possible  number : "))  
new=''
for i in range(9,-1,-1):
    c=str(n).count(str(i))
    new+=str(i)*c
print(new)


#smallest to largest(using looping)
n=int(input("Enter the number to be converted to smallest possible number:"))
new=''
for i in range(1,10):
    c=str(n).count(str(i))
    new+=str(i)*c
print(new)

#largest to smallest(using list)
n=int(input("Enter the number to be converted into largest possible  number : "))  
l=list(str(n))
l.sort()
new=""
l.reverse()
for i in l:
    new+=i
print(int(new))



#smallest to largest(using list)(with string logic)
n=int(input("Enter the number to be converted into smallest possible  number : "))  
l=list(str(n))
l.sort()
new=""
for i in l:
    new+=i
print(int(new))


#smallest to largest(using list)
n=int(input("Enter the number to be converted into smallest possible  number : "))  
l=list(str(n))
l.sort()
new=0
for i in l:
    new=new*10+int(i)
print(new)



n=int(input("Enter the number to be checked: "))
b=(n)
count=0
for i in b:
    if i==1:
        c+=1
if c%2==0:
    print("It is an Evil number")
else:
    print("It is not an Evil number")
    
    
    

n=int(input("Enter the number to be checked: "))
count =0
for i in str(bin(n)):
    if i=="1":
        count+=1
if count%2 != 0:
    print("It is an ODIOUS number")
else:
    print("It is not a ODIOUS number")


n=int(input("Enter the number to be checked: "))
count =0
for i in bin(n)[2:]:
    count+=int(i)
if count%2 != 0:
    print("It is an ODIOUS number")
else:
    print("It is not a ODIOUS number")

#way to convet integer into binary
n=int(input("Enter the number to be checked: "))
a=n
binary=''
while a>0:
    binary+=str(a%2)
    a//=2
print("The binary equivalent:",binary[::-1])





n=int(input("Enter the number to be checked: "))
a=0
b=1
while a<n:
    c=a+b
    a=b
    b=c
    print(a)
if n==a:
    print("It is in fibonacci series")
else:
    print("It is not in fibonacci series ")
    
    
    

#tribonacci
n=int(input("Enter the number to be checked"))
a=0
b=1
c=1
while a<n:
    d=a+b+c
    a=b
    b=c
    c=d
if n==a:
    print("It is in tribonacci series")
else:
    print("It is not in tribonacci series")
    
    
    
    

n=int(input("Enter the number to be checked: "))
flag = False
temp=n
for i in range(50):
    if str(temp)[::-1]==str(temp):
        flag=True
        break
    else:
        temp=int(str(temp))+int(str(temp)[::-1])
if flag == True :
    print("It is a LYCHREL number in the first 50 iterations")
else:
    print("It is not a LYCHREL number in the first 50 iterations ")




n=int(input("Enter the number:"))
check=0
length=len(str(n))
for i in str(n):
    if i=='0' or n%int(i)==0:
        check+=1
if check==length:
    print("It is a good number")
else:
    print("It is not a good number")


#good number
a=int(input("Enter the first number in range:"))
b=int(input("Enter the second number in range:"))
c=0
print("The good numbers are:")
for n in range(a,b+1):
    check=0
    length=len(str(abs(n)))
    for i in str(abs(n)):
        if i=='0' or n%int(i)==0:
            check+=1
    if check==length:
        print(n)
        c+=1
print("Number of good numbers:",c)





















