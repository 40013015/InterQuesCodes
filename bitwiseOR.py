''' take the array of strings stored in strArr, which will only contain two strings of equal length
that represent binary numbers, and return a final binary string that performed the bitwise OR operation on both strings.
A bitwise OR operation places a 0 in the new string where there are zeroes in both binary strings, otherwise it places a 1 in that spot. For example: if strArr is ["1001", "0100"] then your program should return the string "1101"
'''

strArr=["1001","1010"]
a, b = list(strArr[0]), list(strArr[1])
res = []
for i in range(0, len(a)):
    x = '0'
    if a[i] == '1' or b[i] == '1':
        x = '1'
    res.append(x)
print(''.join(res))


'''def BitwiseOne(strArr):
  out=''
  for i in range(len(strArr[0])):
    if strArr[0][i] == '1' or strArr[1][i] == '1':
      out+='1'
    else:
      out+='0'
    
  # code goes here
  return out

# keep this function call here 
print(BitwiseOne(input()))'''