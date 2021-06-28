def powerofTwo(num):
    while num%2==0:
        num=num/2
        print(num)
    if num==1:
        return True
    else:
        return False
print(powerofTwo(int(input())))