def Pyramid (height,symbol = "#"):
    pyramidStr = ""
    base = height * 2
    offset = base // 2
    for layer in range(1,height+1):
        for blank in range(0,offset-layer):
            pyramidStr+=" "
        for blank in range(layer,((layer-1)*2)+layer+1):
            pyramidStr+=symbol
        pyramidStr+="\n"


    return  pyramidStr

height = int(input("Pyramid height? "))
print(Pyramid(height))
