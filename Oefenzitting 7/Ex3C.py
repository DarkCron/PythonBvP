import string
def SubString(sub,str):
    sub = sub.lower()
    str = str.lower()
    length = len(str)
    if len(str) < len(sub):
        return -1
    elif str[0:len(sub)]== sub:
        return 0
    else:
        result = SubString(sub,str[1:len(str)])
        if result == -1:
            return -1
        else:
            return SubString(sub,str[1:len(str)]) +1

print(SubString("can", "Can you can a can as a canner can can a can?"))
print(SubString("a can", "Can you can a can as a canner can can a can?"))

print(SubString("you", "Can you can a can as a canner can can a can?"))
print(SubString("tin", "Can you can a can as a canner can can a can?"))
