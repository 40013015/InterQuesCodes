'''return the string true if the characters a and b are separated by exactly 3 places anywhere in the string at least once
(ie. "lane borrowed" would result in true because there is exactly three characters between a and b). Otherwise return the string false.'''

def ABCheck(string):
    for i in range(len(string)):
        print(string[i+4])
        if string[i] == 'a' and string[i+4] == 'b':
          return 'true'
        if string[i] == 'b' and string[i+4] == 'a':
          return 'true'
    return 'false'

# keep this function call here
print(ABCheck(input()))