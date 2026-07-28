
#SORTING THE NAME IN ALPHABETIC ORDER THEN DISPLAYING IT WITH ITS NUMBER
n=int(input("Enter the number of entries you want to enter: "))
d={}
for i in range(n):
    name=input("Enter the name: ")
    mob=int(input("Enter the mobile no: "))
    d[name]=mob
k=sorted(d.keys())
e={}
for i in k:
    e[i]=d[i]
print(e)  



#SEARCH THE NAME OF THE COUNTRY AND IT WILL TELL IF ANY OF THE SEVEN WONDERS ARE PRESENT THEIR OR NOT
d={"mexico":"chichen itza",
   "brazil":"christ the redeemer",
   "india":"taj mahal",
   "china":"great wall of china",
   "peru":"machu picchu", 
   "jordar":"petra",
   "italy":"colosseum"}
country=input("Enter the name of the country: ")
flag=False
for i in d:
    if i==country:
        flag=True
        break
    else:
        continue
if flag == True:
    print("Seven wonder: ",d[i])
else:
    print("Not Found")
    
""" for i in d.items():
     print(i)
     
 ('mexico', 'chichen itza')
 ('brazil', 'christ the redeemer')
 ('india', 'taj mahal')
 ('china', 'great wall of china')
 ('peru', 'machu picchu')
 ('jordar', 'petra')
 ('italy', 'colosseum')       """



"""for i,j in d.items():
    print(i,j)

mexico chichen itza
brazil christ the redeemer
india taj mahal
china great wall of china
peru machu picchu
jordar petra
italy colosseum     """


































































