def pal(string):
    new=string.replace(" ","")
    if new==new[::-1]:
        return "true"
    else:
        return "false"

print(pal(input()))