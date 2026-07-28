#almost same as normal file handeling 



#Write in a file
import pickle as p
f=open("file.dat","wb")
s="My name is shivatmika"
p.dump(s,f)
f.close()



#Read a file
import pickle as p
f=open("file.dat","rb")
s=p.load(f)
print(s)
f.close()


#Reading form files
import pickle as p

def insert():
    f=open('Employees.dat','ab')
    empid=int(input('ENTER Employee id:'))
    name=input('Enter Employee name:')
    dept=input('Enter Department:')
    sal=int(input('Enter the Salary:'))
    employee_data=[empid,name,dept,sal]
    p.dump(employee_data,f)
    f.close()

def display():
   f=open('Employees.dat','rb')
   try:
       while True:
           l=p.load(f)
           print(l)
   except EOFError:
       f.close()

def update():
    f=open('Employees.dat','rb+')
    try:
        while True:
            beginningofline=f.tell()
            l=p.load(f)
            if l[1]=='rajveer':
                l[-1]=25000
            f.seek(beginningofline)
            p.dump(l,f)
    except EOFError:
        f.close()

    

#QUESTION 


import pickle as p
def write():
    f=open("employees.dat","ab")
    while True:
        ide=int(input("Enter your ID:"))
        dep=int(input("Enter your department:"))
        sal=int(input("Enter your salary:"))
        exp=int(input("Enter your years of experience:"))
        p.dump([ide,dep,sal,exp],f)
        
        while True:
            ch=input('Do you want to enter more records?Press Y for Yes, N for No:')
            if ch[0] in 'yYnN':
                if ch[0] in 'yY':
                    break
                if ch[0] in 'nN':
                    f.close()
                    return
            else:
                print('Invalid choice! Please try again...')
write()    
    
    
def step1():
    f=open("employees.dat","rb")
    try:
        while True:
            l=p.load(f)
            print(l)
    except EOFError:
        f.close()
step1()


def step2():
    f=open("employees.dat","rb")
    try:
        while True:
            l=p.load(f)
            if l[-1]!=0 or l[-2]!=0:
                print(l)
    except EOFError:
        f.close()
step2()
    
def step3():
    f=open("employees.dat","rb")
    main=[]
    try:
        while True:
            l=p.load(f)
            main.append(l)
    except EOFError:
        pass
    department=[]
    print("Department\tNumber of employees\tTotal salary\tAverage salary")
    for i in main:
        noE=0
        tot=0
        avg=0
        for j in main:
            if i[1]==j[1]:
                noE+=1
                tot+=j[2]
            try:    
                avg=tot//noE
            except:
                pass
        if i[1] not in department:
            department.append(i[1])    
            print(i[1],"\t\t\t",noE,"\t\t\t\t\t",tot,"\t\t\t",avg)
step3()


def step4():
    f=open("employees.dat","rb")
    d={}
    try:
        while True:
            l=p.load(f)
            d[l[0]]=l[2]
    except:
        pass
    sort=list(d.items())
    print(sort)
    for i in range(len(sort)-1):
        for j in range(len(sort)-1-i):
            if sort[j][1]<sort[j+1][1] or (sort[j][1]==sort[j+1][1] and sort[j][0]>sort[j][0]):
                sort[j],sort[j+1]=sort[j+1],sort[j]
    print(sort)
step4()    



'''AN EXAMPLE OF THIS BINARY SORTING (used in the question)
employees = {
    "Alice": 50000,
    "Bob": 81000,
    "Charlie": 62000,
    "David": 81000,
    "Eva": 68000
}
l=list(employees.items())
for i in range(len(l)-1):
    for j in range(len(l)-1-i):
        if l[j][1]<l[j+1][1] or (l[j][1]==l[j+1][1] and l[j][0].lower()>l[j][0].lower()):
            l[j],l[j+1]=l[j+1],l[j]
 '''     



"""Question """

import pickle as p
def modify():
    f=open("employees.dat","rb")
    main=[]
    try:
        while True:
            l=p.load(f)
            if l[3]>=10:
                l[2]+=l[2]*(10/100)
            elif 5<=l[3]<=9:
               l[2]+=l[2]*(5/100)
            main.append(l) 
    except EOFError:
        f.close()
    print(main)
    f=open("employees.dat","wb")
    for i in main:
        p.dump(i,f)
    f.close()
modify()













































































      