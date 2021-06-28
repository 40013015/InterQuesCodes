arr=[1,42,421,124]
print(max(arr))
print(min(arr))
if len(arr) == 2:
    maxi = max(arr)
    mini = min(arr)
    print( str(maxi) + ' ' + str(mini))
else:
    maxi = max(arr)
    mini = min(arr)
    # print (maxi,mini)
    arr1 = [i for i in arr if i != maxi and i != mini]
    print( str(min(arr1)) + ' ' + str(max(arr1)))

