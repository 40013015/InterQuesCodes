string1=str(input())
li=string1.split()
print(li)
max=0
for i in li:
    for letter in i:
        if letter.isalpha() and len(i)>=max:
            max=len(i)
            longest=i
# noinspection PyUnboundLocalVariable
print(longest)


# or
def LongestWord(sen):
    # code goes here
    no_spaces = ""
    not_letter_list = []
    word_list = []
    letter_count = 0
    answer = ""

    # find characters that aren't letters
    no_spaces = sen.replace(' ', '')
    for character in no_spaces:
        if not character.isalpha():
            not_letter_list.append(character)
            print(not_letter_list)

    # replace non letter characters with a space
    for item in not_letter_list:
        sen = sen.replace(item, ' ')
    print(sen)

    word_list = sen.split()

    for word in word_list:
        if len(word) > letter_count:
            answer = word
            letter_count = len(word)

    return answer


# keep this function call here
print(LongestWord(input()))
