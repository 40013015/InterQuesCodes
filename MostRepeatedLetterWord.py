'''take the str parameter being passed and return the first word with the greatest number of repeated letters.
For example: "Today, is the greatest day ever!" should return greatest because it has 2 e's (and 2 t's) and it comes before ever
which also has 2 e's. If there are no words with repeating letters return -1. Words will be separated by spaces.'''

def LetterCount(str):

  # code goes here
  maxLetters = 1
  greatestWord = ''
  myWords = str.split()

  for word in myWords:
    for letter in word:
      if word.count(letter) > maxLetters:
        maxLetters = word.count(letter)
        greatestWord = word
  if maxLetters == 1:
    return '-1'
  else:
    return greatestWord



  #return str

# keep this function call here
print(LetterCount(input()))