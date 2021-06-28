'''greater repeated letter word'''
string1="Hello apple pie"
s1=string1.split(' ')
repeated=1
nonrep=-1
for word in s1:
    for i in word:
        if word.count(i) > repeated:
            repeated = word.count(i)
            nonrep=word
print(nonrep)




'''def LetterCountI(str):
  words = str.split(' ')
  most_repeated = 1
  answer = -1

  for word in words:
    for i in word:
      if word.count(i) > most_repeated:
        most_repeated = word.count(i)
        answer = word

  return answer
# keep this function call here 
print(LetterCountI(input()))'''