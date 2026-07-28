s=int(input("Enter the time in seconds:"))
h=s//3600
s%=3600
m=s//60
s=s%60
print("Time taken: ",h,"hr",m,"min",s,"sec")
