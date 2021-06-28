'''return the string true if there is an equal number of x's and o's, otherwise return the string false.
Only these two letters will be entered in the string, no punctuation or numbers. For example:
if str is "xooxxxxooxo" then the output should return false because there are 6 x's and 5 o's.'''

string=str(input())
count1=0
count2=0
for i in string:
    if i=='x':
      count1+=1
    elif i=='o':
      count2+=1
if count1==count2:
    print ("true")
else:
    print("false")

#or
def ExOh(string):
  count1=0
  count2=0
  for i in string:
    if i=='x':
      count1+=1
    elif i=='o':
      count2+=1
  if count1==count2:
    return "true"
  else:
    return "false"

# keep this function call here
print(ExOh(input()))