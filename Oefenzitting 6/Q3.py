# Use the function in Question 2 to write a program that builds word vocabulary from a se-
# quence of texts.  The program should have a loop allowing the user to type texts.  The loop
# finishes when user types “QQQ". Whenever the program reads a text, it updates the vocabu-
# lary, then prints the new vocabulary size, the list of newly added words. After the user types
# “QQQ", the program prints the list of words occurring in more than 50% of the input texts.

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

def updateVoc(newSet, finalSet,recordSet):
    print("Words newly added: ",end="")
    for word in newSet:
        recordSet.add(word)
        if not word in finalSet:
            print("'",word,"'",sep= "",end = ", ")
            finalSet.add(word)

    print("\nNew size of the vocabulary: ",len(finalSet))

    return

completeVoc = set()
finalVoc = set()
inp = input("String here: ")
inpAmount = 1
while inp != "QQQ":
    updateVoc(generateVocabulary(cleanWord(inp)),finalVoc,completeVoc)
    inp = input("String here: ")
    inpAmount += 1

print("Words occurring in at more than 50% of the input texts: ")
commonWords = set()
for word in finalVoc:
    count = 0
    for w in completeVoc:
        if word == w:
            count+=1
        if count >= inpAmount/2:
            commonWords.add(w)
            break

for w in commonWords:
    print(w,end=" ")