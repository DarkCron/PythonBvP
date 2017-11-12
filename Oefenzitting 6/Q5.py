convDict = {"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"A":10,"B":11,"C":12,"D":13,"E":14,"F":15}

def convertHex(str):
    length = len(str)-1
    count = 0
    num = 0
    for c in str:
        num += int(convDict[c] * (16 ** (length - count)))
        count+=1
    return num

print(convertHex("D2A1F"))