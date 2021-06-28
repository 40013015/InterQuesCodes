def NumberAddition(strParam):
    str1 = strParam.replace(' ', '')
    nonalpha = []
    for i in str1:
        if not i.isalpha():
            nonalpha.append(int(i))
        print(nonalpha)

    # code goes here
    return sum(nonalpha)


# keep this function call here
print(NumberAddition(input()))

''' if str is "88Hello 3World!" the output should be 91. You will have to differentiate between single digit numbers and multiple digit numbers
like in the example above. 
So "55Hello" and "5Hello 5" should return two different answers. Each string will contain at least one letter or symbol.'''
def NumberAddition(str1):
    print(set(str1))
    for char in set(str1):
      if not char.isdigit():
          str1 = str1.replace(char, ' ')
      print("digit set is:"+str1)
    return sum(map(int, str1.split())) #converting string elements into int using list(str1.split())

# keep this function call here
print(NumberAddition(input()))