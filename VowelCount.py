def Vowelcount(string1):
    count = 0
    for i in string1:
        if i in "aeiouAEIOU":
            count += 1
    return count


print(Vowelcount(input()))
