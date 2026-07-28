#ALL WORDS IN REVERSE ORDER
s=input("Enter the word: ")
print(s[::-1])


s=input("Enter the word: ")
for i in s[::-1]:
    print(i,end="\n")



#PRINT ODD INDEX
s=input("Enter the word: ")
for i in s:
    index=i.index()
    if index%2 == 0:
        continue
    else:
        print(i)
 
    
    
#PRINT EVEN INDEX
s=input("Enter the word: ")
for i in s:
    ind=s.index(i)
    if ind%2 == 0:
        print(i)



#PRINT INDEX ,ASCII VALUE AND THE NUMBER ITSELF
s=input("Enter the word: ")
for i in s:
    ind=s.index(i)
    print(ind,i,ord(i))
#ord()------>CONVETS STRING INTO INTS ASCII VALUE



#PRINT THE SAME THING ABOVE BUT IN REVERSE ORDER
s=input("Enter the word: ")
for i in s[::-1]:
    print(s.index(i),i,ord(i))



#INPUT A SENTENCE AND REVERSE IT
s=input("Enter the sentence: ").strip()
l=[]
l=s.partition(" ")
for i in l:
    print(i[::-1],end=" ")


#PALINDROME OR NOT
s=input("Enter the sentence: ").strip()
if s == s[::-1]:
    print("Yes, this is a Palindrome number")
else:
    print("No, this ia not a Palindrome number")


#COUNT NUMBER OF SPACES
s=input("Enter the sentence: ")
c=0
for i in s:
    if i == " ":
        c+=1
print("The number of spaces in the string: ",c)
        


#COUNT AND DISPLAY NUMBER OF LETTERS
s=input("Enter the sentence: ").strip()
c=0
for i in s:
    if i.isalpha() == True:
        c+=1
        print(i)
print("Total number of alphabets: ",c)



#COUNT AND DISPLAY NUMBER OF NUMBERS
s=input("Enter the sentence: ").strip()
c=0
for i in s:
    if i.isdigit() == True:
        c+=1
        print(i)
print("Total number of digits: ",c)



#UPPER CASE AND LOWER CASE LETTERS
s=input("Enter the sentence: ")
u=l=0
for i in s:
    if i.isupper():
        u+=1
    elif i.islower():
        l+=1
print("Upper case characters: ",u)
print("Lower case characters: ",l)



#COUNT THE NUMBER OF VOWALS
s=input("Enter the word: ")
v=0
for i in s:
    if i in "AEIOUaeiou":
        v+=1
        print(i)
print(v)



#COUNT THE NUMBER OF CONSONENTS
s=input("Enter the word: ")
c=0
for i in s:
    if i not in "AEIOUaeiou":
        c+=1
        print(i)
print(c)



#DISPLAY THE WORD WITH ITS ALPHABETICAL ORDER INDEX
s=input("Enter the word: ").upper()
for i in s:
    print(i,ord(i)-64)


s=input("Enter the word: ")
for i in s:
    print(i,ord(i.upper())-64)


#DISPLAY AFTER REPLACING THE CONSONENTS BY THE LETTER FOLLOWING IT
s=input("Enter the word: ")
c=""
for i in s:
    if i not in "AEIOUaeiou":
        c+=chr(ord(i)+1)
    else:
        c+=i
print(c)



#SORT AND DISPLAY THE LETTERS IN APLHABETICAL ORDER
s=input("Enter the word: ").upper()
l=list(s)
l.sort()
for i in l:
    print(i,ord(i)-64)



#UNIQUE WORD OR NOT
s=input("Enter the word: ")
flag= True
for i in s:
    for j in s:
        if i == j:
            flag=False
if flag == True:
    print("It is a unique number")
else:
    print("It is not a unique number")



#QUESTION 45,70,80,86

#REPLACE ALL DOUBLE LETTERS WITH A SINGLE ONE 
s=input("Enter the sentence: ").upper()+' '
n=""
i=0
while i<len(s)-1:
    if s[i] == s[i+1]:
        n+=s[i]
        i+=1
    else:
        n+=s[i]
    i+=1
print(n)
    


#REVERSE THE ORDER OF ITS WORDS
s=input("Enter the sentence: ").upper()
p=s.split(" ")
print(p[::-1])




#DISPLAY THE WORD WITH THE HIGHEST LENGTH
s=input("Enter the sentence: ").upper()
p=s.split(" ")
print('Word with maximum characters:',max(p,key=len))
#p.sort(key=len)

s=input("Enter the sentence: ").upper()
p=s.split(" ")
n=''
for i in p:
    if len(i)>len(n):
        n=i
print('Word with maximum characters:',n)




#CONVERT THE WORD INTO A PALINDROME WORD
s=input("Enter the word: ").upper()
n=""
n=s+s.rstrip(s[-1])[::-1]
print(n) 































































