def Balance(string):
    if len(string) == 0:
        return True
    if len(string) <= 1:
        return (string[0] != "(" and string[0]!= ")")
    lastOpenBracket = 0
    for c in range(0, len(string)):
        if string[c] == "(":
            lastOpenBracket = c
        else:
            break

    if string[lastOpenBracket] == "(":
        if string[lastOpenBracket+1] == ")":
            if lastOpenBracket == 0:
                return Balance(string[lastOpenBracket+2:len(string)])
            if lastOpenBracket != 0:
                return Balance(string[0:lastOpenBracket] + string[lastOpenBracket+2:len(string)])
        else:
            for c in range(0,len(string)):
                if string[c] != "(":
                    return Balance(string[0:c] + string[c+1:len(string)])
                    break;
    else:
        return Balance(string[1:len(string)])


print(Balance(":-)"))