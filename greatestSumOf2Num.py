'''take the array of integers stored in arr, and determine if any two numbers (excluding the first element)
in the array can sum up to the first element in the array. For example: if arr is [7, 3, 5, 2, -4, 8, 11],
then there are actually two pairs that sum to the number 7: [5, 2] and [-4, 11]. Your program should return all pairs, with the numbers separated by a comma, in the order the first number appears in the array.
Pairs should be separated by a space. So for the example above, your program would return: 5,2 -4,11'''

import numpy
from itertools import permutations
n=[17, 4, 5, 6, 10, 11, 4, -3, -5, 3, 15, 2, 7]
arr=numpy.array(n)
print(arr)

def TwoSum(arr1):

  res = []                    #empty list to store group of 2Nums for grestest num add answer
  s = arr[0]
  for i in range(1, len(arr)-1):
    x = arr[i]
    print("Value of x is:",x)
    #print(i+1)
    for j in range(i+1, len(arr)):
      print("value of x+arr[j] is:",x+arr[j])
      if x + arr[j] == s:
        res.append(str(x)+","+str(arr[j]))
        print(res)
  if len(res) > 0:
    return " ".join(res)
  else:
    return "-1"

# keep this function call here
print(TwoSum(arr))
