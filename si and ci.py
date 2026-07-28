p=int(input("Enter principale amount "))
r=int(input("Enter rate "))
t=int(input("Enter time "))
s=(p*r*t)/100
c=p*((1+r/100)**t)-p
print("The simple interest is:",s)
print("The compound interest:",c)
