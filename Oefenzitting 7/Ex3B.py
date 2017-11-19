import string
def SubString(sub,str):
    sub = sub.lower()
    str = str.lower()
    if len(str) < len(sub):
        return False
    elif str[0:len(sub)]== sub:
        return True
    else:
        return SubString(sub,str[1:len(str)])

print(SubString("boards", "How many boards could the Mongols hoard if the Mongol hordes got bored"))
print(SubString("Mongol hordes", "How many boards could the Mongols hoard if the Mongol hordes got bored"))

print(SubString("Bored", "How many boards could the Mongols hoard if the Mongol hordes got bored"))
print(SubString("Dinner plate", "How many boards could the Mongols hoard if the Mongol hordes got bored"))
