#SOMETHINGS about file handeling 
#if we use 'w' or 'w+' mode then the existing contents of the file are lost
#if we use 'r' or 'r+' then the existing contents of the file remain
#in append the lines remain and the new word is added at the end of the existing file 
#tell()---> position of the file pointer 
#seek()--->puts the file pointer wherever we want 


#WRITE
f=open('file.txt','w')
f.write("My name is Shivatmika")
f.close()  #must close to save the contents in the file or it remains blank




#READ
f=open('file.txt','r')
s=f.read()
print(s)
f.close()




#APPEND
f=open('file.txt','a')
f.write("My name is Shiva")
f.close()



#READ AND WRITE
f=open('file.txt','r+')
f.write("i am")   
print(f.read())
f.close()
'''shows the file contents which are not changed , for eg if we changed
the 0th index the file will be visible in read from the 1st index'''




#WRITE AND READ
f=open('file.txt','w+')
f.write("My name is Shiva")
print(f.tell())     #tells where the pointer is
f.seek(0)
print(f.read()) 
f.close()
'''so here initally when we did not use seek 
nothing was visible in read as the files first clears its contents 
and then goes to the end pointer, to cahnge that we used seek() this function
takes the file to the pointer we want it to be . Bacause of which not the read()
function() displayes all its contents from 0th index to the end'''




#READ LINE ONE BY ONE
f=open('file.txt')
while True:
    s=f.readline()#now this variable stores a single line at a time 
    print(s)
    if s=='':
        break
f.close()




#READ LINE BY PUTTING ALL THE LINES IN A LIST
f=open('file.txt')
l=f.readlines()#now this variaavle stores a list in which all lines are ele of the list
for i in l:
    print(i)
f.close()





#WRITES THE LIST ITEMS AS LINES 
f=open('file.txt','w')
line=["spiderman\n","ironman\n","thor\n"]
f.writelines(line)
f.close()





#THIS IS A DIFFERENT WAY FOR FILE HANDELING- here we dont have to close the file as it behaves as a module
with open("example.txt", "r") as file:
    first_line = file.readline()
    print(first_line)
    
    
    
  
'''QUESTION==Creat a script to make a text file named as file.txt now accept the sentence
form the user and store it an a text file.Now extract the content of the file,
count and display the number of spaces in it'''

f=open("file.txt","w+")
s=input("Enter the content of the file: ")
f.write(s)
f.seek(0)
s1=f.read()
c=0
for i in s1:
    if i == " ":
        c+=1
print("The number of spaces in the text are: ",c)
f.close()




'''QUESTION==Write a Python function that display the the number of time the word "python" 
appears in the text file named "Prog.txt"'''

f=open("Prog.txt","r")
s=f.read()
l=s.split(" ").lower()
c=0
for i in l:
    if i == "python":
        c+=1
print("The number of time ""python"" appears: ",c)
f.close()




'''QUESTION==Write and call a Python function to read lines from 
a text file STORIES.TXT and display those lines which doesn't 
start with a vowal '''

with open("STORIES.TXT","r") as f:
    line=f.readlines()
    for i in line:
        if i[0] not in "AEIOUaeiou":
            print(i)

            
                

'''Question '''
#1
def readrecords():
    with open("logs.txt","r")as f:
        print(f.read())
readrecords()

#2
def totalscore():
    with open("logs.txt","r+") as f:
        l=f.readlines()
        name=[]
        for i in range(len(l)):
            r=l[i].split(" ")
            sm=int(r[1])
            for j in l[i+1:]:
                s=j.split(" ")
                if r[0] == s[0]:
                    sm+=int(s[1])
            if r[0] not in name:
                print(r[0],sm)
                name.append(r[0])
totalscore()         


#2
def total():
    with open("logs.txt","r") as f:
        l=f.readlines()
        d={}
        for sen in l:
            rec=sen.split(" ")
            if rec[0] in d:
                d[rec[0]]+=int(rec[1])
            else:
                d[rec[0]]=int(rec[1])
    return d

#total() 
def show():
    d=total()
    for i,j in d.items():
        print(i,j)  
show()

#3
def remove():
    original=total()
    resultant={}
    for i,j in original.items():
        if j > 60:
            resultant[i]=j
    #print(resultant)
    with open("logs.txt","w+")as f:
        s=''
        for i in resultant:
            s+=str(i)+" "+str(resultant[i])+'\n'
        s=s.rstrip('\n')
        f.write(s)
        f.seek(0)
        print(f.read())
remove()     
        
        
def remove2():
    original=total()
    resultant={}
    updated=[]
    for i,j in original.items():
        if j > 60:
            resultant[i]=j
    with open("logs.txt","r") as f:
        l=f.readlines()
        for i in range(len(l)):
            j=l[i].rstrip().split(" ")
            if j[0] in resultant:
                updated.append(l[i])
    with open("logs.txt","w") as f:   
        f.writelines(updated)
remove2()


l=[45,56,78,98,65]
for i in range(len(l)):
    print(l[i])
    if i==2:
        l.pop(i)
    
        
remove2()


def sort():
    d=total()
    new={}
    with open("logs.txt","w")as f:
        for i,j in d.items():
            k=d.keys()
            v=d.values()
            sort(l)
        for i in range(len(v)):
            for j in range(len(k)):
                if v[i] == d.get(k[j]):
                    new[k[j]]=v[i]
         f.write(new) 
         
               
                   

































































