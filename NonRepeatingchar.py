str1="agettkhkkngaeee"
for char in str1:
    print(str1.count(char))
    if str1.count(char)<2:
        print("Non repeated letter is:",char)