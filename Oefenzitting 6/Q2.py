import string
def cleanWord(w):
    return w.lower().strip(string.punctuation)

def generateVocabulary(str):
    strSet = set()
    strSet = str.split(" ")
    properSet = set()
    for word in strSet:
        if not word in properSet:
            properSet.add(word)
    return properSet

def printVoc(strSet):
    print("Vocabulary: ",end = "")
    for w in strSet:
        print(w,", ",end = " ")
    return

inp = input("String here: ")
printVoc(generateVocabulary(cleanWord(inp)))