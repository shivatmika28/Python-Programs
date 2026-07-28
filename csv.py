#WRITING 
import csv
f=open("File.csv","w",newline="")
w=csv.writer(f)
header=["RollNo.","Student Name","Marks"]
row1=[1,"Shaurya",99.7]
row2=[2,'Aditya',94.5]
row3=[3,'Tejas',9.6]
row4=[4,'Priyanshi',98.2]
w.writerows([header,row1,row2,row3,row4])
f.close()

#READING
import csv
f=open('File.csv')
r=csv.reader(f)
for i in r:
    print(i)
f.close()


"""QUESTION 1"""


import csv
# Data to be written
data = [
    ["EmployeeID", "Name", "Department", "Salary", "ProjectsCompleted", "Rating"],
    [101, "Alice", "AI", 85000, 8, 4.5],
    [102, "Bob", "Web", 72000, 5, 3.8],
    [103, "Charlie", "AI", 91000, 10, 4.9],
    [104, "David", "Cloud", 68000, 3, 2.9],
    [105, "Eva", "Web", 75000, 6, 4.1],
    [106, "Frank", "AI", 91000, 10, 4.9],
    [107, "Grace", "Cloud", 90000, 9, 4.8],
    [108, "Helen", "Web", 45000, 1, 2.5]
]

# Open the CSV file in write mode
with open("employees.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)

print("employees.csv created successfully!")

def step1():
    f=open("employees.csv","r")
    l=csv.reader(f)
    for i in l:
        print(i)
    f.close()
step1()
            
def step2():
    f=open("employees.csv","r")
    l=csv.reader(f)
    header=next(l)
    print(header)
    for i in l:
        if int(i[3])>50000 and float(i[5])>3.0:
                print(i)
    f.close()
step2()

def step3():
    f=open("employees.csv","r",newline="")
    main=[]
    try:
        while True:
            l=csv.reader(f)
            main.append(l)
    except EOFError:
        pass
    department=[]
    print("Department\tNumber of employees\tTotal salary\tAverage salary")
    for i in main:
        noE=0
        tot=0
        avg=0
        rating=0
        for j in main:
            if i[2]==j[2]:
                noE+=1
                tot+=j[3]
                if 
            try:    
                avg=tot//noE
            except:
                pass
        if i[1] not in department:
            department.append(i[1])    
            print(i[1],"\t\t\t",noE,"\t\t\t\t\t",tot,"\t\t\t",avg)

def divide(a, b):
   '''if b == 0:
      raise ValueError("Cannot divide by zero")'''
   return a / b

try:
   result = divide(10, 0)
except Exception as e:
   print(e)


try:
    a=int(input('Enter the first number:'))
    b=int(input('Enter the second number:'))
    c=a/b
    print(c)
except Exception as e:
    print(e)
else:
    print('Operation successfully completed')
finally:
    print('Thank You!!!')

