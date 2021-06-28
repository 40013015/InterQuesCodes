'''Replace every letter in the string with the letter following it in the alphabet (ie. c becomes d, z becomes a).
Then capitalize every vowel in this new string (a, e, i, o, u) and finally return this modified string.'''

string=str(input())
result=""
for x in string:
    if x == "z":
        newChar="a"
    elif x == "Z":
        newChar = "A"
    elif x.isalpha():
      newChar = chr(ord(x) + 1)
      print((ord(x)))
      print(chr(ord(x)))
    else:
      newChar = x

    if newChar in "aeiou":
      newChar = newChar.upper()
    result = result + newChar
print(result)


