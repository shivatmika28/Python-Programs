#INPUT IN A LIST
n=int(input('How many elements do you want to enter?'))
l=[]
for i in range(n):
    ele=int(input('Enter the element'+str(i)+':'))
    l.append(ele)
print(l)



# the input should be a list
l=eval(input('Enter the list:'))
print(l)
print(type(l))



n=int(input("How many elements do you want to enter:"))
l=[]
for i in range(n):
    ele=int(input("Enter the element: "+str(i+1)+":"))
    l.append(ele)
print(l[::-1])


#input should be a list
l=eval(input("Enter the list to be reversed:"))
#l.reverse()--->we dont use this as the list itself is reversed but we dont want that
print(l[::-1])

#PRINT EVEN ELEMENTS
n=int(input("How many elements do you want to enter:"))
l=[]
for i in range(n):
    ele=int(input("Enter the element: "+str(i+1)+":"))
    l.append(ele)
e=[]
for i in l:
    if i%2==0:
        e.append(i)
print("All even elements in the list are ",e)



l=eval(input("Enter the list"))
e=[]
for i in list:
    if i%2==0:
        e.appent(l[i])
print("All even elements in the list are ",e)


#PRINT ODD ELEMENTS
n=int(input("How many elements do you want to enter:"))
l=[]
for i in range(n):
    ele=int(input("Enter the element: "+str(i+1)+":"))
    l.append(ele)
o=[]
for i in l:
    if i%2!=0:
        o.append(l[i])
print("All odd elements in the list are ",o)


#PRINT EVEN INDEX ELEMENTS
n=int(input("How many elements do you want to enter:"))
l=[]
for i in range(n):
    ele=int(input("Enter the element: "+str(i+1)+":"))
    l.append(ele)
e=[]
for i in range(len(l)):
    if i%2==0:
        e.append(l[i])
print("the even index elements are ",e)




n=int(input("How many elements do you want to enter:"))
l=[]
for i in range(n):
    ele=int(input("Enter the element: "+str(i+1)+":"))
    l.append(ele)
print("the even index elements are ",l[::2])


#PRINT ODD INDEX ELEMENTS
n=int(input("How many elements do you want to enter:"))
l=[]
for i in range(n):
    ele=int(input("Enter the element: "+str(i+1)+":"))
    l.append(ele)
o=[]
for i in range(len(l)):
    if i%2!=0:
        o.append(l[i])
print("the odd index elements are ",e)


#PRINT ODD AND EVEN INDEX ELEMENTS
n=int(input("How many elements do you want to enter:"))
l=[]
for i in range(n):
    ele=int(input("Enter the element: "+str(i+1)+":"))
    l.append(ele)
e=o=[]
for i in range(len(l)):
    if i%2==0:
        e.append(l[i])
    else:
        o.append(l[i])
print("the even index elements are ",e)
print("The odd index elements are ",o)


#PRINT THE AVERAGE OS ALL ELEMENTS IN THE LIST
n=int(input("How many elements do you want to enter:"))
l=[]
for i in range(n):
    ele=int(input("Enter the element: "+str(i+1)+":"))
    l.append(ele)
s=avg=0
for i in l:
    s+=i
avg=s/len(l)
print("The average of all elements in the list is:",avg)

n=int(input("How many elements do you want to enter:"))
l=[]
for i in range(n):
    ele=int(input("Enter the element: "+str(i+1)+":"))
    l.append(ele)
s=sum(l)
avg=s/len(l)


#SUM OF ALL 1 DIGIT ELEMENTS AND ALL 2 DIGIT ELEMENTS
n=int(input("How many elements do you want to enter:"))
l=[]
for i in range(n):
    ele=int(input("Enter the element: "+str(i+1)+":"))
    l.append(ele)
dig1=dig2=[]
for i in l:
    if i%10==i:
        dig1.append(i)
    elif i%100==i:
        dig2.append(i)
print("One digit elements are ",dig1)
print("Two digit elements are ",dig2)



#PERFECT SQUARE
n=int(input("How many elements do you want to enter:"))
l=[]
for i in range(n):
    ele=int(input("Enter the element: "+str(i+1)+":"))
    l.append(ele)
perfect=[]
for i in l:
    if int(i**(1/2))-(i**(1/2))==0:  #i**0.5%1==0
        perfect.append(i)
print("All the Perfect Squares in the list are:",perfect)



#PRIME NUMBERS
n=int(input("How many elements do you want to enter:"))
l=[]
for i in range(n):
    ele=int(input("Enter the element: "+str(i+1)+":"))
    l.append(ele)
prime=[]
for i in l:
    f=0
    for j in range(1,i+1):
        if i%j==0:
            f+=1
    if f==2:        
        prime.append(i)
print("The prime elements in the list are:",prime)


#PALINDROME NUMBERS
n=int(input("How many elements do you want to enter:"))
l=[]
for i in range(n):
    ele=int(input("Enter the element: "+str(i+1)+":"))
    l.append(ele)
pal=[]
for i in l:
  if str(i)==str(i)[::-1]:
        pal.append(i)
print("The palindrome elements in the list are:",pal)


#INC ALL ELE BY 10%
n=int(input("How many elements do you want to enter:"))
l=[]
for i in range(n):
    ele=int(input("Enter the element: "+str(i+1)+":"))
    l.append(ele)
new=[]
for i in l:
    i+=i*(10/100)
    new.append(i)
print("The elements of the list after 10% inc.",new)


#LINEAR SEARCH
n=int(input("Enter the number of elements u want to enter:"))
l=[]
for i in range(n):
    ele=int(input("Enter the element: "+str(i+1)+":"))
    l.append(ele)
s=int(input("Enter the number to be searched: "))
ind=-1
for i in range(len(l)):
    if (l[i]==s):
        ind=i
        break
if ind != -1:
    print("The entered element is in the list at index:",ind)
else:
    print("The element is not in the list")



n=int(input("Enter the number of elements u want to enter:"))
l=[]
for i in range(n):
    ele=int(input("Enter the element: "+str(i+1)+":"))
    l.append(ele)
s=int(input("Enter the number to be searched: "))
ind=l.index(s)
if ind != -1:
    print("The entered element is present in the list at index: ",ind)
else:
    print("Entered element is not found in the list")




#FREQUENCY OF THE ELEMENT
n=int(input("Enter the number of elements u want to enter:"))
l=[]
for i in range(n):
    ele=int(input("Enter the element "+str(i+1)+":"))
    l.append(ele)
s=int(input("Enter the number to be searched: "))
freq=0
for i in l:
    if i==s:
        freq+=1
if freq==0:
    print("Element does not exist in the list")
else:
    print("Element exists with a Frequency:",freq)


n=int(input("Enter the number of elements u want to enter:"))
l=[]
for i in range(n):
    ele=int(input("Enter the element "+str(i+1)+":"))
    l.append(ele)
s=int(input("Enter the number to be searched: "))
freq=l.count(s)
if freq==0:
    print("Element does not exist in the list")
else:
    print("Element exists with a Frequency:",freq)



#BINARY SEARCH
n=int(input("Enter the number of elements u want to enter:"))
l=[]
for i in range(n):
    ele=int(input("Enter the element "+str(i+1)+":"))
    l.append(ele)
s=int(input("Enter the number to be searched: "))
#we can use l.sort() here but the user will give the elements in ascending order so we dont have to
beg=0
end=len(l)-1
ind=-1
while beg <= end:
    mid=(beg+end)//2
    if s == l[mid]:
        ind=mid
        break
    elif s < l[mid]:
        end=mid-1
    elif s > l[mid]:
        beg=mid+1
if ind != -1:
    print("The entered element is present at index: ",ind)
else:
    print("The given element is not present")



#COPY THE LIST IN ANOTHER ARRAY AND DISPLAY
n=int(input("Enter the number of elements u want to enter:"))
l=[]
for i in range(n):
    ele=int(input("Enter the element "+str(i+1)+":"))
    l.append(ele)
m=[]   #U CAN USE m.copy(l)
for i in l:
    m.append(i)
print(m)



#SUM OF TWO LISTS IN ANOTHER LIST
p=eval(input('Enter the first list:'))
q=eval(input('Enter the second list:'))
r=[]
if len(p) == len(q):
    for i in range(len(p)):
        r.append(p[i]+q[i])
else:
    print("Both the list have different lengths")


#PUT ELEMENTS OF BOTH THE LISTS IN ONE LIST ONE AFTER ANOTHER
#if lists are p and q -------> we use r.extend(p) then r.extend(q)
#or a for loop to put individual elements 



#PUT ELEMENTS OF BOTH LISTS IN A WAY THAT FIRST ELE OF LIST 1 THEN LIST 2 THEN LIST ONE AGAIN
p=eval(input('Enter the first list:'))
q=eval(input('Enter the second list:'))
r=[]
for i in range(len(p)+len(q)):
    if i<len(p) and i<len(q):
        r.append(p[i])
        r.append(q[i])
    elif i<len(p):
        r.append(p[i])
    elif i<len(q):
        r.append(q[i])


p=eval(input('Enter the first list:'))
q=eval(input('Enter the second list:'))
r=[]
for i in range(min(len(p),len(q))):
    r.append(p[i])
    r.append(q[i])
r.extend(p[i:])
r.extend(q[i:])



#question l=38,67,78,80,84

#SHIFT THE ELEMENTS ITS INDEX+1 AND FOR THE LAST ONE PUT IN IN 1ST
n=int(input("Enter the number of elements you want to enter: "))
l=[]
for i in range(n):
    ele=int(input("Enter the element: "))
    l.append(ele)
print([l[-1]]+l[:-1])
#       ^---------we have used the external [] to convert the integer into a list
#We have made no changes to the elements in the list 


n=int(input("Enter the number of elements you want to enter: "))
l=[]
for i in range(n):
    ele=int(input("Enter the element: "))
    l.append(ele)
l=[l[-1]]+l[:-1]
print(l)


n=int(input("Enter the number of elements you want to enter: "))
l=[]
for i in range(n):
    ele=int(input("Enter the element: "))
    l.append(ele)
last=l.pop()
l.insert(0,last)
print(l)


n=int(input("Enter the number of elements you want to enter: "))
l=[]
for i in range(n):
    ele=int(input("Enter the element: "))
    l.append(ele)
m=l.copy()
p=l[0]
for i in range(len(l)):
    if len(l)-1>i:
        l[i]=m[i+1]
    else:
        l[i]=p
print(l)


n=int(input("Enter the number of elements you want to enter: "))
l=[]
for i in range(n):
    ele=int(input("Enter the element: "))
    l.append(ele)
p=l[-1]
for i in range(-1,-len(l),-1):
    l[i]=l[i-1]
l[0]=p
print(l)





#FIND THE CELING OF A VALUE(nearest value greater than or equal to the element enterted)
n=int(input("Enter the number of elements you want to enter: "))
l=[]
for i in range(n):
    ele=int(input("Enter the element: "))
    l.append(ele)
val=int(input("Enter the value: "))
l.sort()    # m=sorted(l)---->new list is made with sorted elements ,no changes in the original list
for i in l:
    if i>=val:
        print("The celing of",val,"is:",i)
        break

#l=list(map(int,input().split()))
#THIS T\IS A BETTER THING TO USE TO TAKE INPUT THAT EVAL FUNCTION







