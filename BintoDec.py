'''Example -: 1011
1). Take modulo of given binary number with 10.
    (1011 % 10 = 1)
2). Multiply rem with 2 raised to the power
    it's position from right end.
    (1 * 2^0)
    Note that we start counting position with 0.
3). Add result with previously generated result.
    decimal = decimal + (1 * 2^0)
4). Update binary number by dividing it by 10.
    (1011 / 10 = 101)
5). Keep repeating upper steps till binary > 0.

Final Conversion -: (1 * 2^3) + (0 * 2^2) +
                 (1 * 2^1) + (1 * 2^0) = 11'''

def bintoDec(num):
    return int(num,2)
print(bintoDec('1000')) #give as a string(dont forget)

num1=123456789
num2=100000
print(float(num1/num2))

num=int(input())
if num>1:
    hours=num//60
    min=num%60
    res=str(hours)+":"+str(min)
print(res)