n=[]
print("Enter the number"+'\n')
ele=input()
a=len(ele)-1
b=0

while a:
    print(b)
    n.append(ele[b]+ele[b+1])
    a=a-1
    b=b+1
print(n)
print(max(n))
