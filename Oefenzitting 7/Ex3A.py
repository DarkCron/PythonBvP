def Reverse(string):
    if(len(string) == 0):
        return string
    if (len(string) == 1):
        return string
    else:
        return Reverse(string[1:len(string)])+string[0]

print(("I can tucan"))
print(Reverse("I can tucan"))