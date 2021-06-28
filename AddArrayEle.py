import numpy
n=[4,6,23,10,1,3]
n.sort()
print(n)
arr=numpy.array(n)
print(arr)
print(format(arr[0:5]))
sum=0
for i in arr[0:5]:
    sum=sum+i
print(sum)
