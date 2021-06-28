str1=str(input())
li=str1.split()
print(li)
newword=[]
for word in li:
    print(word[0].upper())
    print(word[1:])
    newword.append(word[0].upper()+word[1:])
print( " ".join(newword))
