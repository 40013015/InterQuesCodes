'''take the array of numbers stored in arr and return the string true if any combination of numbers in the array (excluding the largest number)
can be added up to equal the largest number in the array, otherwise return the string false.
For example: if arr contains [4, 6, 23, 10, 1, 3] the output should return true because 4 + 6 + 10 + 3 = 23.
The array will not be empty, will not contain all the same elements, and may contain negative numbers.'''

import itertools
arr=[4,6,23,10,1,3]

s = max(arr)
arr.remove(s)
comb = []
for i in range(len(arr) + 1):
    for se in itertools.combinations(arr, i):
        comb.append(se)
print(comb)
for x in comb:
    while sum(x) == s:
        print('true')
        break

print( 'false')
