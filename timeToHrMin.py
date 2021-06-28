value=int(input())
hours=value//60 #print whole number adjusted in float(ex:2.6 as 2)
print(hours)
minutes=value%60 #print reminder of x/y
print(minutes)
res=str(hours)+":"+str(minutes)
print(res)
