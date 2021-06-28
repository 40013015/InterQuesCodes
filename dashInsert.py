def DashInsertII(s):
    s = list(str(s))
    print(s)
    for i in range(len(s) - 1):
        if s[i] in "13579" and s[i + 1] in "13579":
            s[i] = s[i] + "-"
        elif s[i] in "2468" and s[i + 1] in "2468":
            s[i] = s[i] + "*"

    # code goes here
    return "".join(s)


# keep this function call here
print(DashInsertII(input()))