'''take the array of numbers stored in arr and return the string "Arithmetic" if the sequence follows an arithmetic
pattern or return "Geometric" if it follows a geometric pattern. If the sequence doesn't follow either pattern return -1.
An arithmetic sequence is one where the difference between each of the numbers is consistent, where as in a geometric sequence,
each term after the first is multiplied by some constant or common ratio. Arithmetic example: [2, 4, 6, 8] and Geometric example: [2, 6, 18, 54].
Negative numbers may be entered as parameters, 0 will not be entered, and no array will contain all the same elements.'''

import numpy


def arithGeo(arr):
    diff = []
    quot = []

    for i in range(1, len(arr)):
        diff.append(arr[i] - arr[i - 1])
        quot.append(arr[i] / arr[i - 1])

    diff_flag = True
    quot_flag = True
    for i in range(1, len(diff)):
        if diff[i] != diff[i - 1]:
            diff_flag = False
        if quot[i] != quot[i - 1]:
            quot_flag = False

    if diff_flag:
        return "Arithmetic"
    elif quot_flag:
        return "Geometric"
    else:
        return -1


# initilizing list
n=int(input("enter number of elements:"))
lst = []
for i in range(n):
    lst.append(int(input()))

# converting list to array
arr = numpy.array(lst)

# displaying list
print("List: ", lst)

# displaying array
print("Array: ", arr)

print(arithGeo(arr))
