'''li=["0100","1000"]
a,b=list(li[0]),list(li[1])
print(a)
res=[]
for i in range(len(a)):
    if a[i] == '1' and b[i] == '1':
        x = '0'
    elif a[i] == '1' and b[i] == '0':
        x='0'
    else:
        x='0'
    res.append(x)
print(''.join(res))'''








'''li=["10100","10000"]
a,b=list(li[0]),list(li[1])
print(a)
res=[]
for i in range(len(a)):
    if a[i]=='1' and b[i]=='1':
        x = '1'
    elif a[i]=='1' and b[i]=='0':
        x  ='1'
    else:
        x='0'
    res.append(x)
print(''.join(res)) '''

def longestword(words):
    nonLetter=[]
    nospaces=""
    nospaces=words.replace(" ","")
    for letter in nospaces:
        if not letter.isalpha():
            nonLetter.append(letter)
            print(nonLetter)

    for item in nonLetter:
        words=words.replace(item,' ')
    print(words)

    new=words.split()
    count=0
    for word in new:
        if len(word)>count:
            ans=word
            count=len(word)
    return ans

print(longestword(input("enter words:")))


import numpy
print(dir(numpy))

